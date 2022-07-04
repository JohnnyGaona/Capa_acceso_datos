from flask import Blueprint,render_template, request
from utils.db import conexion

cmp_prodcuto = Blueprint("cmp_prodcuto",__name__)
cursor = conexion.cursor()

@cmp_prodcuto.route("/updateCMP_Product")
def update ():
    return "actualizando compatibilidad"

@cmp_prodcuto.route("/newCMP_Product",methods=["POST"])
def add():
    x = int()
    cursor.execute('insert into compatibilidad_producto(id,id_producto,producto_compatible) values(?,?,?);', (request.form['id_com'],request.form['Producto id'],request.form['referencias id']))
    conexion.commit()
    return "guardando compatibilidad"

@cmp_prodcuto.route("/deleteCMP_Product")
def delete():
    id = input("id del producto: ")
    cursor.execute('delete from compatibilidad_producto where id = ?',id)
    return "Eliminando compatibilidad"

@cmp_prodcuto.route("/viewCMP_Product")
def view():
    cursor.execute("SELECT * FROM compatibilidad_producto")
    rows = cursor.fetchall()
    for row in rows:
     print(row)
    return "mostrando compatibilidad"

@cmp_prodcuto.route("/maincmp_pro")
def principal():
    return render_template("compatibilidad.html")

def datos ():
    id_con = input("Ingrese el codigo de la categoria: ")
    id_pro = input("ingrese id de prodcuto: ")
    id_com_pro = input("ingrese id de prodcuto copatible: ")
    cursor.execute("update compatibilidad_producto set id_producto=?, producto_compatible=? where id=?",(id_pro,id_com_pro,id_con))