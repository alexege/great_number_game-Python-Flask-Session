from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    session['block-visibility'] = 'none'
    if not session['randNumber'] in session:
        session['randNumber'] = random.randint(1,100)
    else:
        print("number on redirect: " + str(session['randNumber']))
        pass
    print("number on page load: " + str(session['randNumber']))
    return render_template('index.html')

@app.route('/guessHigh')
def playerGuessHigh():
    session['block-color'] = 'red'
    session['guess-message'] = 'Too High'
    print("Guessed High")
    return render_template('index.html')

@app.route('/guessLow')
def playerGuessLow():
    session['block-color'] = 'red'
    session['guess-message'] = 'Too low'
    print("Guessed Low")
    return render_template('index.html')

@app.route('/winner')
def playerWin():
    session['block-color'] = 'green'
    session['guess-message'] = str(session['randNumber']) + " was the number!"
    return render_template('index.html')

@app.route('/getVals', methods=["POST"])
def getVals():
    session['block-visibility'] = 'block'
    print("Our guess: " + str(request.form['guess']))
    print("Number to guess: " + str(session['randNumber']))
    tempVar = request.form['guess']
    if int(tempVar) == session['randNumber']:
        return redirect('/winner')
    elif int(tempVar) > session['randNumber']:
        return redirect('/guessHigh')
    elif int(tempVar) < session['randNumber']:
        return redirect('/guessLow')
    else:
        return redirect('/guess')
if __name__=="__main__":
    app.run(debug=True)