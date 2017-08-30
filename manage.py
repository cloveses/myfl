import pickle
import random
from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = 'lkdjkjf&*^%&(*(*))(775$%^^**(*_+&**&GBHJB'

txt = [('select','Jinja2 uses a central object?','A item','B item','C item','D item','A'),
        ('select','2 Jinja2 uses a central object?','A item','B item','C item','D item','A'),
        ('select','3 Jinja2 uses a central object?','A item','B item','C item','D item','A'),
        ('yorn','The simplest way to configure Jinja2 y','Y'),
        ('yorn','2The simplest way to configure Jinja2 n','N')]

def get_exam(exams):
    if exams:
        exam = exams[0]
        exams = pickle.dumps(exams[1:])
        return exam, exams

@app.route("/hh")
def hh():
    flag = request.args.get('change', '')
    if flag != 'next':
        if 'curr_exam' in session:
            exam = pickle.loads(session['curr_exam'])
            return render_template('index.html',exam=exam)
    if 'exams' not in session:
        exams = txt[:]
        random.shuffle(exams)
    else:
        exams = pickle.loads(session['exams'])
    res = get_exam(exams)
    if res:
        exam, exams = res
        session['exams'] = exams
        session['curr_exam'] = pickle.dumps(exam)
        return render_template('index.html',exam=exam)
    return render_template('score.html',score='90')

@app.route("/hc")
def hc():
    return request.args.get('key', '')

if __name__ == '__main__':
    app.run(debug=True)