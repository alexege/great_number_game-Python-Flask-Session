from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if not session['randNumber'] in session:
        session['randNumber'] = random.randint(1,100)
    else:
        print("number on redirect: " + str(session['randNumber']))
        pass
    print("number on page load: " + str(session['randNumber']))
    return render_template('index.html')


@app.route('/getVals', methods=["POST"])
def getVals():
    print("Our guess: " + str(request.form['guess']))
    tempVar = request.form['guess']
    if int(tempVar) == session['randNumber']:
        print("WINNER!")
    else:
        print("Loser!")
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)