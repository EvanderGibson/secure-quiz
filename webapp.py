import os
from flask import Flask, url_for, render_template, request, redirect, session
import time

app = Flask(__name__)

app.secret_key = os.environ["SECRET_KEY"]

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear()
    return redirect(url_for('renderMain'))

@app.route('/page1')
def renderPage1():
    session["startTime"] = time.time()
    return render_template('page1.html')

@app.route('/page2', methods=['GET', 'POST'])
def renderPage2():
    if request.method == 'POST':
        if "answer1" not in session:
            session["answer1"] = request.form['answer1']
        return redirect(url_for('renderPage2'))
    return render_template('page2.html')
    
@app.route('/page2.5', methods=['GET', 'POST'])
def renderPage25():
    if request.method == 'POST':
       if "answer2" not in session:
            session["answer2"] = request.form['answer2']
       return redirect(url_for('renderPage25'))
    return render_template('page2.5.html')   

@app.route('/page3', methods=['GET', 'POST'])
def renderPage3():
    if request.method == 'POST':
        if "answer3" not in session:
            session["answer3"] = request.form['answer3']
        session["endTime"] = time.time()
        return redirect(url_for('renderPage3'))
    score=0
    if session["answer1"] == "cloud":
        score = score + 1
    if session["answer2"] == "keyboard":
        score = score + 1
    if session["answer3"] == "tomorrow":
        score = score + 1
    
    total_time = session.get("endTime", time.time()) - session.get("startTime", time.time()) 
    
    var = session.get("answer1") == "cloud"
    yart = "true" if var else "false"
    pablo = session.get("answer2") == "keyboard"
    prunice = "true" if pablo else "false"
    voweltowel = session.get("answer3") == "tomorrow"
    clambert = "true" if voweltowel else "false"
    return render_template('page3.html', cloud=session.get("answer1"), TorF=yart, yotalyime=str(round(total_time,1)), ovulatina=prunice, keyboard=session.get("answer2"), tomorrow=session.get("answer3"), hyjinkrat=clambert, splooge=score)

if __name__ == "__main__":
    app.run(debug=True)