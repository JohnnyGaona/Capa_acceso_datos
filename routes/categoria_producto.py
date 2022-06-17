from flask import Blueprint,render_template, request
from utils.db import conexion

ca_producto = Blueprint("ca_producto",__name__)
cursor = conexion.cursor()

@ca_producto.route("/updateCA_Product")
def update ():
    datos()
    return "actualizando categoria del prodcuto"

@ca_producto.route("/newCA_Product", methods=['POST'])
def add():
    cursor.execute('insert into producto_categoria(id, categoria) values(?,?);', (request.form['id'],request.form['categoria']))
    conexion.commit()
    return "guardando categoria del prodcuto"

@ca_producto.route("/deleteCA_Product")
def delete():
    id = input("id del producto: ")
    cursor.execute('delete from producto_categoria where id = ?',id)
    return "Eliminando categoria del prodcuto"

@ca_producto.route("/viewCA_Product")
def view():
    cursor.execute("SELECT * FROM producto_categoria")
    rows = cursor.fetchall()
    for row in rows:
     print(row)

    return "mostrando categoria del prodcuto"

@ca_producto.route("/mainca_pro")
def principal():
    return render_template("categoripro.html")

def datos ():
    id_con = input("Ingrese el codigo de la categoria: ")
    nombre = input("nombre de la categoria: ")
    cursor.execute("update producto_categoria set  categoria=? where id=?",(nombre,id_con))