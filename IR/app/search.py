# PROCESSING
import re
from lists import stop_words, synonym_list, syn_popularity, times, gte, lte, all_lists, fields_ori, names, bio_list
from elasticsearch import Elasticsearch, helpers
import queries
from helper import calSimilarity_words

client = Elasticsearch(HOST="http://localhost",PORT=9200)
INDEX = 'index-ministers'

#function for stemming the word
def stemming(word):
    stem_dictionary = {"ගේ$":"","^(සිටි||හිටි).$":"සිටි"}
    stemmed = word
    for k in stem_dictionary:
      stemmed = re.sub(k,stem_dictionary[k],stemmed)
    return stemmed


#function for pre-processing the phase
def preprocess(phrase):
    phrase_list = phrase.split()
    processed_phrase = []

    for word in phrase_list:
      stemmed_word = word
      if not word.isdigit():
        stemmed_word = stemming(word)
      if stemmed_word not in stop_words:
        processed_phrase.append(stemmed_word)

    processed_s = " ".join(processed_phrase)
    return processed_s


#boosting function
def boost(boost_array):
    name ="name^{}".format(boost_array[1])
    position = "position^{}".format(boost_array[2])
    party = "party^{}".format(boost_array[3])
    district = "district^{}".format(boost_array[4])
    related_subjects = "related_subjects^{}".format(boost_array[5])
    biography = "biography^{}".format(boost_array[6])
    
    return [name, position, party, district, related_subjects, biography]


#function for search using the name
def searchByName(tokens):
  found = 0
  for t in range(len(tokens)):
    token = tokens[t]

    for name in names:
      name_list = name.split()
      for i in range(len(name_list)):
        if calSimilarity_words(token, name_list[i], 0.8) and abs(len(token)-len(name_list[i])) <= 1:
            tokens.append(name_list[i])
            found = 1
  if found:
    return True
  else:
    return False


def search(phrase):
    # 0 - number
    # 1 - name
    # 2 - position
    # 3 - party
    # 4 - district
    # 5 - related_subjects
    # 6 - biography
    flags = [0, 1, 1, 1, 1, 1, 1]

    #search list
    # 0 - position
    # 1 - party
    # 2 - district
    # 3 - related_subjects
    # 4 - contact info
    # 5 - participation
    search_list = [0, 0, 0, 0, 0, 0]

    num=0
    processed_phrase = preprocess(phrase)
    tokens = processed_phrase.split()
    search_by_name = searchByName(tokens)
    tokens = list(set(tokens))
    containsDigit = bool(re.search(r'\d', processed_phrase))

    if search_by_name:
      flags[1] = 5
      for word in tokens:
        for i in range(len(synonym_list)):
          if word in synonym_list[i]:
            print('Boosting field', i, 'for', word, 'in synonym list - search by name')
            search_list[i] = 1
            break

    elif containsDigit: #check number
      popularity = False
      participation = False
      before_birth = False

      for word in tokens:
        if word.isdigit():
          flags[0] = 1
          num = int(word)
          if(len(word) == 4):
            before_birth = True
        else:
          if word in syn_popularity:
                popularity = True
          elif word in times:
                op="eql"
                participation = True
                if word in gte:
                  op = 'gte'
                elif word in lte:
                  op = 'lte'

    else: #not name or not a digit
      # Identify numbers
      search_terms = []
      for w in range(len(tokens)):
          word = tokens[w]

          # Check whether a value from any list is present
          for i in range(len(all_lists)):
              l =  all_lists[i]
              for term in l:
                ts = term.split()
                for j in range(len(ts)):
                  if calSimilarity_words(word, ts[j]):
                    # tokens[w] = ts[j]
                    search_terms.append(ts[j])
                    print('Boosting field',i+2,'for',word,ts[j],'in all list')
                    flags[i+2] = 5
                    

          # Check whether token matches any synonyms
          for i in range(4):
              if word in synonym_list[i]:
                  print('Boosting field', i, 'for', word, 'in synonym list')
                  flags[i+2] = 5

      tokens = search_terms
    fields = boost(flags)


    phrase = " ".join(tokens)
    print(phrase, fields, search_list)

    if flags[1] == 5: #if have a name
            query_body = queries.exact_match(phrase)
            res = client.search(index=INDEX, body=query_body)
            resl = res['hits']['hits']
            print(resl)
            outputl = []
            for hit in resl:
              minister = hit['_source']
              name = minister["name"]
              age = minister["age"] # need to add
              birthday = minister["birthday"] # need to add
              position = minister["position"]
              party = minister["party"]
              district = minister["district"]
              contact = ";".join(minister["contact_information"])
              related_subjects = ";".join(minister["related_subjects"])
              biography = minister["biography"]
              outputl.append([name, position, party, district, contact, related_subjects, biography])
            res = outputl
    elif flags[0] == 1: #If there is a number
        if popularity:
          print('Making Range Query for popularity')
          query_body = queries.agg_multi_match_and_sort_q(phrase, num, fields)
          res = client.search(index=INDEX, body=query_body)
          resl = res['hits']['hits']
          outputl = []
          for hit in resl:
              outputl.append(str(hit['_source']['overall_rank'])+ " - " +hit['_source']['name'])
          res = outputl   
        elif participation:
          if op != "eql":
            print('Making Range Query for participation with '+op)
            query_body = queries.agg_multi_match_and_sort_q(phrase, num, fields, op,"participated_in_parliament")
            res = client.search(index=INDEX, body=query_body)
          else:
            print("exact match")
            required_field = "participated_in_parliament"
            query_body = queries.exact_match(phrase, required_field, search_val = num)
            res = client.search(index=INDEX, body=query_body)
          resl = res['hits']['hits']
          outputl = []
          for hit in resl:
              outputl.append(hit['_source']['name']+" ("+ str(hit['_source']['participated_in_parliament']) +" වතාවක්)")
          res = outputl 
        elif before_birth :
          print('Making Range Query for before birth ')
          query_body = queries.agg_multi_match_and_sort_q(phrase, num, fields, 'lte',"birth_year")
          res = client.search(index=INDEX, body=query_body)
          resl = res['hits']['hits']
          outputl = []
          for hit in resl:
              outputl.append(hit['_source']['name'] )
          res = outputl 
    else:
        if(flags.count(5) == 2):
          required_field2 = ["biography","district"]
          query_body = queries.cross_q(phrase,required_field2)
          res = client.search(index=INDEX, body=query_body)
          resl = res['hits']['hits']
          outputl = []
          for hit in resl:
              outputl.append(hit['_source']['name'] )
          res = outputl 
        else:
          print('Making Faceted Query') #no name and other field search
          query_body = queries.agg_multi_match_q(phrase, fields)
          required_field = fields_ori[flags.index(5)-2]
          res = client.search(index=INDEX, body=query_body)
          resl = res['hits']['hits']
          outputl = []
          for hit in resl:
              ansl = hit['_source'][required_field]
              if isinstance(ansl,list):
                out = " ; ".join(ansl)
              else:
                out = ansl
              outputl.append([hit['_source']['name']+" - "+ str(out),hit['_score']])
              # outputl.append([hit['_source']['name'],hit['_score']])
          res = outputl 
    return res
