from flask import Blueprint,render_template, request
from utils.db import conexion

producto = Blueprint("producto",__name__)
cursor = conexion.cursor()

@producto.route("/updateUser")
def update ():
    datos()
    return "actualizando producto"

@producto.route("/newProduct",methods=["POST"])
def add():
    cursor.execute('insert into producto(nombre, precio, descripción, id_categoria, stock) values(?,?,?,?,?);', (request.form['nombre'],request.form['precio'],request.form['descripcion'],request.form['id_categoria'],request.form['stock']))
    conexion.commit()
    return "guardando prodcuto"

@producto.route("/deleteProduct")
def delete():
    id = input("id del producto: ")
    cursor.execute('delete from producto where id = ?',id)
    return "Eliminando prodcuto"

@producto.route("/viewProduct")
def view():
    cursor.execute("SELECT * FROM producto")
    rows = cursor.fetchall()
    for row in rows:
     print(row)
    return "mostrando prodcuto"

@producto.route("/mainPro")
def principal():
    return render_template("producto.html")

def datos ():
    ci_con = input("Ingrese el codigo del producto: ")
    nombre = input("nombre: ")
    precio = input("precio: ")
    descripcion = input("descripcion: ")
    id_categoria = input("id de la categoria: ")
    stock = input("stock: ")
    cursor.execute("update producto set  nombre=?, precio=?, descripción=?, id_categoria=?, stock=? where id=?",(nombre,precio,descripcion,id_categoria,stock,ci_con))