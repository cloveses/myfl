import pickle
from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = 'lkdjkjf&*^%&(*(*))(775$%^^**(*_+&**&GBHJB'

@app.route("/hh")
def hh():
    content = [('A','jjdhhd'),('B','uuuehd')]
    session['keyy'] = pickle.dumps(content)
    return render_template('index.html')

@app.route("/hc")
def hc():
    print(pickle.loads(session['keyy']))
    
    return request.args.get('key', '')

if __name__ == '__main__':
    app.run(debug=True)