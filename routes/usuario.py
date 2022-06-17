from flask import Blueprint, render_template, request
from utils.db import conexion

usuario = Blueprint("usuario",__name__)
cursor = conexion.cursor()

@usuario.route("/updateUser")
def update_usuario ():
    datos()
    return "Actualizando usuario"

@usuario.route("/newUser", methods=['POST'])
def add_usuario():
    cursor.execute('insert into usuario(id, nombre, direccion, ciudad, email, telefono, usuario, contraseña, id_roll) values(?,?,?,?,?,?,?,?,?);', (request.form['ci'],request.form['nombre'],request.form['direccion'],request.form['ciudad'],request.form['email'],request.form['telefono'],request.form['usuario'],request.form['contraseña'],request.form['id_roll']))
    conexion.commit()
    return "guardando usuario"

@usuario.route("/deleteUser")
def delete_usuario():
    ci = input()
    cursor.execute('delete from usuario where id = ?',ci)
    return "Eliminando usuario"

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
    nombre = input("nombre: ")
    direccion = input("direccion: ")
    ciudad = input("ciudad: ")
    email = input("email: ")
    telefono = input("telefono: ")
    usuario = input("Usuario: ")
    contraseña = input("contraseña: ")
    id_roll = int(input("roll: "))
    cursor.execute("update usuario set  nombre=?,direccion=?,ciudad=?,email=?,telefono=?,usuario=?,contraseña=?,id_roll=? where id=?",(nombre,direccion,ciudad,email,telefono,usuario,contraseña,id_roll,ci_con))