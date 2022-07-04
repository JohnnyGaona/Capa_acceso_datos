from flask import Blueprint, render_template, request
from utils.db import conexion
from utils.Cedula import verificar
from utils.numero import numero
from utils.corre import correo
import os

usuario = Blueprint("usuario",__name__)
cursor = conexion.cursor()

@usuario.route("/updateUser")
def update_usuario ():
    datos()
    return "Actualizando usuario"

@usuario.route("/newUser", methods=['POST'])
def add_usuario():
    x = verificar(request.form['ci'])
    if x == 1:
        if numero(request.form['telefono']):
            if correo(request.form['email']):
                cursor.execute('insert into usuario(id, nombre, direccion, ciudad, email, telefono, usuario, contraseña, id_roll) values(?,?,?,?,?,?,?,?,?);', (request.form['ci'],request.form['nombre'],request.form['direccion'],request.form['ciudad'],request.form['email'],request.form['telefono'],request.form['usuario'],request.form['contraseña'],request.form['id_roll']))
                conexion.commit()
                return "guardando usuario"
            else:
                return "Error... no se pudo guardar el dato"
        else: 
            return "Error... no se pudo guardar el dato"
    else:
        return "Error... no se pudo guardar el dato"
    

@usuario.route("/deleteUser")
def delete_usuario():
    ci = input()
    x=verificar(ci)
    if x ==1:
        cursor.execute("select * from usuario where id=?",ci)
        registro = cursor.fetchall()
        if registro :
            cursor.execute('delete from usuario where id = ?',ci)
            return "Eliminando usuario"
        else: 
            return "Registro no encontrado en la BD"
    else:
        return "Cedula incorrecta"

@usuario.route("/viewUser")
def view_usuario():
    cursor.execute("SELECT * FROM usuario")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    return "mostrando usuario"

@usuario.route("/mainU")
def principal():
    return render_template("usuario.html")


def datos ():
    ci_con = input("Ingrese el codigo del usuario: ")
    x = verificar(ci_con)
    if x == 1:
        cursor.execute("select * from orden where id=?",id)
        registro = cursor.fetchall()
        if registro :
            flag = False
            nombre = input("nombre: ")
            direccion = input("direccion: ")
            ciudad = input("ciudad: ")
            while flag != True:
                os.system ("cls")
                email = input("email: ")
                flag = correo(email)
            flag = False
            while flag != True:
                os.system ("cls")
                telefono = input("telefono: ")
                flag = numero(telefono)
            usuario = input("Usuario: ")
            contraseña = input("contraseña: ")
            id_roll = int(input("roll: "))
            cursor.execute("update usuario set  nombre=?,direccion=?,ciudad=?,email=?,telefono=?,usuario=?,contraseña=?,id_roll=? where id=?",(nombre,direccion,ciudad,email,telefono,usuario,contraseña,id_roll,ci_con))
        else: 
            print("Registro no encontrado en BD") 
    else:
        print("Cedula incorrecta")