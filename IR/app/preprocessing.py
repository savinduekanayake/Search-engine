import re
from helper import calSimilarity_words
from lists import stop_words

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