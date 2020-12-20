import os  # Para generar el aleatorio
# importer el modulo sqlite3
import sqlite3
# importer modulo de error de sqlite3
from sqlite3 import Error
# acede a los valores de las variables enviadas por los HTML.
from flask import Flask, request, render_template, redirect, url_for, current_app, g
# importar el encriptador de datos
from werkzeug.security import generate_password_hash, check_password_hash


def get_db():
    try:
        if 'db' not in g:
            g.db = sqlite3.connect('database.db')
        return g.db
    except Error:
        print(Error)


def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()


def insertUsuarios(correo, contrasena):
    hashed_password = generate_password_hash(contrasena)
    db = get_db()
    db.execute(
        "INSERT INTO usuarios (correo, contraseña) VALUES ('%s','%s')" % (
            correo, hashed_password)
    )

    db.commit()
#     print("P2")


def auth_user(correo, contrasena):
    db = get_db()

    res = db.execute( "SELECT count(id) from usuarios where correo='%s'"  % (correo) )

    print(res)
    res_fetch2 = res.fetchall()
    
    print(res_fetch2)

    if res_fetch2[0][0] == 1:
        res = db.execute("SELECT contraseña from usuarios where correo='%s'"  % (correo) )
        res_fetch = res.fetchall()[0][0]
        print(res_fetch)
        print( check_password_hash(res_fetch, contrasena) )

        return check_password_hash(res_fetch, contrasena)
    else:
        return False;



# def insertImagenes(nombre, archivo, usuario):
#     db = get_db()
#     db.execute(
#         "INSERT INTO imagenes (nombre, archivo, usuario) VALUES ('%s','%s','%s')" % (
#             nombre, archivo, usuario)
#     )

#     db.commit()
#     print("P2")
