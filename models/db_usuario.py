from utils.db import db

class usuario (db.Model):
   ci = db.Column(db.String(20), primary_key=True)
   nombre = db.Column(db.String(20))
   direccion = db.Column(db.String(100))
   ciudad = db.Column(db.String(50))
   email = db.Column(db.String(50))
   telefono = db.Column(db.String(15))
   usuario = db.Column(db.String(50))
   contraseña = db.Column(db.String(50))
   id_roll = db.Column(db.Intiger)

   def __init__(self,ci,nombre,direccion,ciudad,email,telefono,usuario,contraseña,id_roll):
      self.ci = ci 
      self.nombre = nombre
      self.direccion = direccion
      self.ciudad = ciudad
      self.email = email
      self.telefono = telefono
      self.usuario = usuario
      self.contraseña = contraseña
      self.id_roll = id_roll