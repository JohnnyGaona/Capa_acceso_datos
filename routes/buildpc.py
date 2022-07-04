from distutils.command.build import build
from flask import Blueprint,render_template, request
from utils.db import conexion
from datetime import datetime

build = Blueprint("build",__name__)
cursor = conexion.cursor()

@build.route("/viewbuild")
def muestra ():
    #Seleccion de la targeta madre 
    cursor.execute("SELECT id, nombre, precio, stock FROM producto where id_categoria='3'")
    rows1 = cursor.fetchone()
    x=0
    print("Targeta madre.....")
    while rows1:
        if rows1[3] !=0:
            x = x+1
            print(x,rows1)
            if x == 1:
                lista = [(x,rows1)]
            else:  
                lista += [(x,rows1)] 

        rows1 = cursor.fetchone()
    
    inp = input("Ingrese la opcion a elegir: ")
    for m in lista:
        sublista = m
        if sublista[0] == int(inp):
            pc = [sublista[1]]
            aux1 = sublista[1]
            tarjeta = aux1[0]
  
    
    #Seleccion de procesador
    cursor.execute("SELECT  producto.id, nombre, precio, stock FROM compatibilidad_producto INNER JOIN producto ON compatibilidad_producto.producto_compatible = producto.id WHERE id_producto = ? AND id_categoria = 1",tarjeta)
    rows2 = cursor.fetchone()
    x=0
    print("Procesador.....")
    while rows2:
        if rows2[3] != 0:
            x = x+1
            print(x,rows2)
            if x == 1:
                lista2 = [(x,rows2)]
            else:  
                lista2 += [(x,rows2)] 

        rows2 = cursor.fetchone()

    inp = input("Ingrese la opcion a elegir: ")
    if lista2: 
        for m in lista2:
            sublista = m
            if sublista[0] == int(inp):
                pc += [sublista[1]]

    #Seleccion de memoria ram
    cursor.execute("SELECT  producto.id, nombre, precio, stock FROM compatibilidad_producto INNER JOIN producto ON compatibilidad_producto.producto_compatible = producto.id WHERE id_producto = ? AND id_categoria = 4",tarjeta)
    rows3 = cursor.fetchone()
    x=0
    print("Memoria RAM....")
    while rows3:
        if rows3[3] !=0:
            x = x+1
            print(x,rows3)
            if x == 1:
                lista3 = [(x,rows3)]
            else:  
                lista3 += [(x,rows3)] 

        rows3 = cursor.fetchone()
    inp = input("Ingrese la opcion a elegir: ")
    for m in lista3:
        sublista = m
        if sublista[0] == int(inp):
            pc += [sublista[1]]

    #Seleccion de disco duro
    cursor.execute("SELECT  producto.id, nombre, precio,stock FROM compatibilidad_producto INNER JOIN producto ON compatibilidad_producto.producto_compatible = producto.id WHERE id_producto = ? AND id_categoria = 5",tarjeta)
    rows4 = cursor.fetchone()
    x=0
    print("Almacenamiento Interno......")
    while rows4:
        if rows4[3] !=0:
            x = x+1
            print(x,rows4)
            if x == 1:
                lista4 = [(x,rows4)]
            else:  
                lista4 += [(x,rows4)] 

        rows4 = cursor.fetchone()

    inp = input("Ingrese la opcion a elegir: ")

    for m in lista4:
        sublista = m
        if sublista[0] == int(inp):
            pc+=[sublista[1]]


    print(" ")
    print("Componentes de la PC")
    total=0
    x=0
    for p in pc:
        x+=1
        print(x,p)
        total = total + p[2]
    print("El coste total por el equipo es de : ",total) 
    inp = input("Desea ordenar el producto: (si/1)(no/0): ")
    
    if inp == '0':
        print("Gracias por su tiempo ")
    else: 
        ci = input("Ingrese su id: ")
        cursor.execute("select * from usuario where id=?",ci)
        registro = cursor.fetchall()
        if registro: 
            estado = "confirmado"
            inp = input("Utilizar mi direccion de cuenta (1) / ingresar una nueva direccion (0): ")

            if inp == '0':
                direccion = input("Nueva direccion: ")
            else:
                cursor.execute("select direccion from usuario where id=?",ci)
                direccion = cursor.fetchone()
            
            fecha = datetime.now()
            cursor.execute('insert into orden(id_comprador, monto, direc_envio, estado_envio, fecha_envio) values(?,?,?,?,?);', (ci,total,direccion[0],estado,fecha))
            conexion.commit()
            print("Orden Realizada....")
            for p in pc:
                cursor.execute("select stock from producto where id=?",p[0])
                stock = cursor.fetchone()
                stock[0]-=1
                cursor.execute("update producto set stock=? where id=?",(stock[0],p[0]))
        else:
            print("No se encontro al usuario....")
    return "Ño"