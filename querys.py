import os
import sqlite3
from sqlite3 import Error
from flask import Flask, request, render_template, redirect, url_for, current_app, g
from db import get_db
from werkzeug.security import generate_password_hash, check_password_hash

def ingresar_usuario(correo, contrasena):
    db = get_db()
    contrasena_encriptada = generate_password_hash(contrasena)
    db.execute(
        "INSERT INTO usuarios (correo, contraseña) VALUES ('%s','%s')" % 
        (correo, contrasena_encriptada)
    )

    db.commit()


def leer_id_usuarios(correo):
    db = get_db()
    res = db.execute(
        "SELECT id FROM usuarios WHERE correo = '%s'" %(
            correo
        )
    )
    return res.fetchall()


def autenticar_usuario(correo, contrasena):
    db = get_db()
    res = db.execute("SELECT count(id) from usuarios where correo='%s'"  % (correo))
    if res.fetchall()[0][0] == 1:
        res = db.execute(
        "SELECT contraseña from usuarios where correo='%s'"  % (correo) )
        return check_password_hash(res.fetchall()[0][0], contrasena)
    else:
        return False



def insertar_imagen(nombre, archivo, usuario,estado, tema):
    db = get_db()
    db.execute(
        "INSERT INTO imagenes (nombre, archivo, id_usuario, estado,descri) VALUES ('%s','%s','%s','%s','%s')" % (
            nombre, archivo, usuario,estado, tema)
    )

    db.commit()


def actualizar_imagen(nombre,archivo,usuario, id):
    db = get_db()
    db.execute(
            
        "UPDATE imagenes SET nombre = '%s', archivo = '%s', usuario = '%s' WHERE id = '%s' " % (
            nombre, archivo, usuario, id)
    )

    db.commit()

def borrar_imagen(id):
    db = get_db()
    db.execute(
            
        "DELETE FROM imagenes WHERE id = '%s'" % (
            id)
    )

    db.commit()

def leer_imagen(id):
    db = get_db()
    res = db.execute(
        "SELECT * FROM imagenes WHERE id_usuario = '%s'" % (
            id
        )
    )
    return res.fetchall()

def buscar(b):
    db = get_db()
    res = db.execute(
        "SELECT * FROM imagenes WHERE nombre = '%s'" % (
            b
        )
    )
    return res.fetchall()