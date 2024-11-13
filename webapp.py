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
        session["answer1"] = request.form['answer1']
        return redirect(url_for('renderPage2'))
    return render_template('page2.html')

@app.route('/page3', methods=['GET', 'POST'])
def renderPage3():
    if request.method == 'POST':
        session["favoriteColor"] = request.form['favoriteColor']
        session["endTime"] = time.time()
        return redirect(url_for('renderPage3'))
    
    total_time = session.get("endTime", time.time()) - session.get("startTime", time.time())
    var = session.get("answer1") == "cloud"
    yart = "true" if var else "false"
    
    return render_template('page3.html', cloud=session.get("answer1"), TorF=yart, yotalyime=total_time)

if __name__ == "__main__":
    app.run(debug=True)