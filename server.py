from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def cycle():
    session['counter'] = 0
    return redirect('/count')

@app.route('/count')
def count():
    session['counter'] += 1
    return render_template('index.html')

@app.route('/increment')
def upTwo():
    session['counter'] += 2
    return render_template('index.html')

@app.route('/reset')
def reset():
    return redirect('/')

app.run(debug=True)
