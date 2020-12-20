import os
import sqlite3
from sqlite3 import Error
from flask import Flask, request, render_template, redirect, url_for, current_app, g
from db import get_db


def insertUsuarios(correo, contrasena):
    db = get_db()
    db.execute(
        "INSERT INTO usuarios (correo, contraseña) VALUES ('%s','%s')" % (
            correo, contrasena)
    )

    db.commit()
    print("P2")


def singUp(correo, contraseña):
    db = get_db()
    res = db.execute(
        "SELECT count(id) from usuarios where correo='%s' and contraseña = '%s'"  % (
            correo, contraseña)
    )
    return res.fetchall()



def insertImagenes(nombre, archivo, usuario):
    db = get_db()
    db.execute(
        "INSERT INTO imagenes (nombre, archivo, usuario) VALUES ('%s','%s','%s')" % (
            nombre, archivo, usuario)
    )

    db.commit()
    print("P2")


def updateImagenes(nombre,archivo,usuario, id):
    db = get_db()
    db.execute(
            
        "UPDATE imagenes SET nombre = '%s', archivo = '%s', usuario = '%s' WHERE id = '%s' " % (
            nombre, archivo, usuario, id)
    )

    db.commit()
    print("P2")

def deleteImagenes(id):
    db = get_db()
    db.execute(
            
        "DELETE FROM imagenes WHERE id = '%s'" % (
            id)
    )

    db.commit()
    print("P2")

def selectImagenes(id):
    db = get_db()
    res = db.execute(
        "SELECT * FROM imagenes WHERE id_usuarios = '%s'" % (
            id
        )
    )
    return res.fetchall()