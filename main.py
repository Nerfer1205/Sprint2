from flask import Flask, render_template, request, redirect, url_for, session
import os
import utils
import querys
import secrets
from werkzeug.utils import secure_filename # para obtener el nombre del archivo de forma segura.

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456678'

@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if querys.autenticar_usuario(email, password):
            res = querys.leer_id_usuarios(email)
            id = res[0][0]
            session['id_usuario'] = id
            return redirect(url_for('welcome'))
        else:
            return render_template('login.html')
    
    else:
        return render_template('login.html')


@app.route('/sign_up' , methods=["GET", "POST"])
def sign_up():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conf_pass = request.form['conf_pass']
        if(password == conf_pass):
            querys.ingresar_usuario(email, password)
        else:
            return render_template('sign-up.html')
        return redirect(url_for('login'))
    
    else:
        return render_template('sign-up.html')


@app.route('/recovery')
def recovery():
    return render_template('recovery.html')

@app.route('/welcome',methods=('GET', 'POST'))
def welcome():
    if request.method == 'GET':
        id_usuario = session['id_usuario']
        res = querys.leer_imagen(id_usuario)
        resLen = len(res)
        return render_template('welcome.html', res = res, resLen = resLen)
    else:
        busqueda = request.form["buscar"]
        res = querys.buscar(busqueda)
        resLen = len(res)
        return render_template('welcome.html', res = res, resLen = resLen)

@app.route('/image',methods=('GET', 'POST'))
def image():
    path = ''
    if request.method == 'POST':
        archivo = request.form["archivo"]
        nombre = request.form["nombre"]
        usuario = session["id_usuario"]
        tema = request.form["tema"]

        try:
            estado = request.form["estado"]
            
        except:
            estado = 'off'
       
        querys.insertar_imagen(nombre, archivo,usuario,estado,tema)
        
    return render_template('actualizate_create.html', path = path) 

@app.route('/download/')
def download():
    return render_template('download.html')

@app.route('/erase')
def erase():
    return render_template('erase.html')