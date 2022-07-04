from flask import Blueprint,render_template, request
from utils.db import conexion

dl_orden = Blueprint("dl_orden",__name__)
cursor = conexion.cursor()

@dl_orden.route("/updateDL_Order")
def update ():
    datos()
    return "actualizando detalle de orden"

@dl_orden.route("/newDL_Order",methods=["POST"])
def add():
    cursor.execute('insert into detalle_orden(id_orden, id_producto, precio_unitario, precio_total, cantidad) values(?,?,?,?,?);', (request.form['id_orden'],request.form['id_prodcuto'],request.form['precio unitario'],request.form['precio total'],request.form['cantidad']))
    conexion.commit()
    return "guardando detalle de orden"

@dl_orden.route("/deleteDL_Order")
def delete():
    id = input("id del detalle de orden: ")
    cursor.execute('delete from detalle_orden where id = ?',id)
    return "Eliminando detalle de orden"

@dl_orden.route("/viewDL_Order")
def view():
    cursor.execute("SELECT * FROM detalle_orden")
    rows = cursor.fetchall()
    for row in rows:
     print(row)   
    return "mostrando detalle de orden"

@dl_orden.route("/mainDl_or")
def principal():
    return render_template("detalleorden.html")

def datos ():
    ci_con = input("Ingrese el codigo del producto: ")
    id_orden = input("id comprador: ")
    id_producto = input("monto: ")
    precio_uni = input("direccion de envio: ")
    precio_to = input("estado de envio: ")
    cantidad = input("Cantidad: ")
    cursor.execute("update detalle_orden set  id_orden=?, id_producto=?, precio_unitario, precio_total, cantidad  where id=?",(id_orden,id_producto,precio_uni,precio_to,cantidad,ci_con))