from flask import Blueprint,render_template, request
from utils.db import conexion


orden = Blueprint("orden",__name__)
cursor = conexion.cursor()

@orden.route("/updateOrder")
def update ():
    datos()
    return "actualizando orden"

@orden.route("/newOrder", methods=["POST"])
def add():
    cursor.execute('insert into orden(id_comprador, monto, direc_envio, estado_envio, fecha_envio) values(?,?,?,?,?);', (request.form['id_comprador'],request.form['monto'],request.form['direccion envio'],request.form['estado envio'],request.form['fecha']))
    conexion.commit()
    return "guardando orden"

@orden.route("/deleteOrder")
def delete():
    id = input("id de la orden: ")
    cursor.execute('delete from orden where id = ?',id)
    return "Eliminando orden"

@orden.route("/viewOrder")
def view(): 
    cursor.execute("SELECT * FROM orden")
    rows = cursor.fetchall()
    for row in rows:
     print(row)
    return "mostrando orden"

@orden.route("/mainOr")
def principal():
    return render_template("orden.html")

def datos ():
    ci_con = input("Ingrese el codigo del producto: ")
    id_comprador = input("id comprador: ")
    monto = input("monto: ")
    direc_env = input("direccion de envio: ")
    estado = input("estado de envio: ")
    cursor.execute("update orden set  id_comprador=?, monto=?, direc_envio=?, estado_envio=?  where id=?",(id_comprador,monto,direc_env,estado,ci_con))