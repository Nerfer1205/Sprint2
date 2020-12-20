from flask import Flask, render_template,request,redirect,url_for
import utils
import querys

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        res = querys.singUp(email, password)
        res_ =res[0][0]
        if res_ == 1:
            return redirect(url_for('welcome'))
        else:
            return render_template('login.html',res = res)
    
    else:
        return render_template('login.html')


@app.route('/sign_up' , methods=["GET", "POST"])
def sign_up():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conf_pass = request.form['conf_pass']
        if(password == conf_pass):
            querys.insertUsuarios(email, password)
        else:
            return render_template('sign-up.html')
        return redirect(url_for('login'))
    
    else:
        return render_template('sign-up.html')


@app.route('/recovery')
def recovery():
    return render_template('recovery.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/image')
def image():
    return render_template('actualizate_create.html')

@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/erase')
def erase():
    return render_template('erase.html')