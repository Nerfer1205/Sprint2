import os
from flask import Flask, render_template,request,redirect,url_for
import utils
import db
FOLDER_CARGA = os.path.abspath("resources") # carpeta donde se cargarán las imágenes.
from werkzeug.utils import secure_filename # para obtener el nombre del archivo de forma segura.

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if querys.autenticar_usuario(email, password):
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

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/image',methods=('GET', 'POST'))  
def image():
    path = ''
    if request.method == 'POST':
        archivo = request.files["archivo"]
        nombre = request.form["nombre"]
        tema = request.form["tema"]
        try:
            estado = request.form["estado"]
        except:
            estado = 'off'
        filename = secure_filename(archivo.filename) # obtener el nombre del archivo de forma segura.
        path = os.path.join(app.config["FOLDER_CARGA"], filename) # ruta de la imagen, incluyendola.
        archivo.save(path)
        flash( 'Imagen guardada con éxito.' )
    return render_template('actualizate_create.html',path = path) 

@app.route('/download')
def download():
    return render_template('download.html')

@app.route('/erase')
def erase():
    return render_template('erase.html')