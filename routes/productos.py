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
    x = float(request.form['precio'])
    if x > 0:
        if int(request.form['stock']) >= 0:
            cursor.execute('insert into producto(nombre, precio, descripción, id_categoria, stock) values(?,?,?,?,?);', (request.form['nombre'],request.form['precio'],request.form['descripcion'],request.form['id_categoria'],request.form['stock']))
            conexion.commit()
            return "guardando prodcuto"
        else:
            return "Error de guardado"
    else:
        return "Error de guardado"

@producto.route("/deleteProduct")
def delete():
    id = input("id del producto: ")
    cursor.execute('delete from producto where id = ?',id)
    return "Eliminando prodcuto"

@producto.route("/viewProduct")
def view():
    cursor.execute("SELECT * FROM producto")
    rows = cursor.fetchone()
    while rows:
        print(rows)
        rows = cursor.fetchone()
    return "mostrando prodcuto"

@producto.route("/mainPro")
def principal():
    return render_template("producto.html")

def datos ():
    ci_con = input("Ingrese el codigo del producto: ")
    nombre = input("nombre: ")
    while precio <= 0:
        precio = input("precio: ")
    descripcion = input("descripcion: ")
    id_categoria = input("id de la categoria: ")
    while stock < 0:
        stock = input("stock: ")
    cursor.execute("update producto set  nombre=?, precio=?, descripción=?, id_categoria=?, stock=? where id=?",(nombre,precio,descripcion,id_categoria,stock,ci_con))