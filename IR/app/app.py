from flask import Flask,render_template,url_for,request,jsonify
from search import search

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',res = None, len=None, num_results=None, message = None)

@app.route('/predictTokens',methods=['POST'])
def predictTokens():
    try:
        if request.method == 'POST':
            message = request.form['message']

            num_results = 0

            if message != "" :
                res = search(message)
                if (len(res) == 0):
                    res = ["ප්‍රතිඵල කිසිවක් හමු නොවීය.."]
                    length = 0
                elif isinstance(res[0],list):
                    length = len(res[0])
                    num_results = len(res)
                else:
                    length = 1
                    num_results = len(res)
                # tokens = []
            else:
                return render_template('home.html',res = None, len=None, num_results=None, message = None)
        return render_template('home.html', res = res, len = length, num_results = num_results, message = message)
    
    except Exception:
        return render_template('home.html',res = None, len=None, num_results=None, message = None)


if __name__ == '__main__':
    # serve(app, host='0.0.0.0', port=8000)
    app.run(debug=True)