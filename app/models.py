from datetime import datetime 
from app import db

class Producto(db.Model):
    __tablename__ = "productos"
    idP = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), unique = True)
    precio = db.Column(db.Numeric(precision= 10,scale=2))
    imagen = db.Column(db.String(100))

class Cliente(db.Model):
    __tablename__ = "clientes"
    idC = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), unique = True)
    contraseña = db.Column(db.String(20), unique = True)
    email = db.Column(db.String(100))

class Venta(db.Model):
    __tablename__ = "ventas"
    idV = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime,default = datetime.utcnow)
    cliente_id = db.Column(db.Integer,db.ForeignKey('clientes.idC'))

class Detalle(db.Model):
    __tablename__ = "detalles"
    idD = db.Column(db.Integer, primary_key = True)
    producto_id = db.Column(db.ForeignKey('productos.idP'))
    venta_id = db.Column(db.Integer,db.ForeignKey('ventas.idV'))
    cantidad = db.Column(db.Integer)


