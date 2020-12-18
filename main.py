from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/sign_up')
def sign_up():
    return render_template('sign-up.html')

@app.route('/recovery')
def recovery():
    return render_template('recovery.html')
