from flask_app import app
from flask import render_template, redirect, session

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hard_reset')
def reset():
    session.clear()
    return redirect('/')