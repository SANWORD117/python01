from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

#creacion y configuracion de la app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost:3306/flask-shopy-2687365'

#crear los objetos de SQLAlchemy y migrate
db = SQLAlchemy(app)
migrate = Migrate(app,db)

#creacion de los modelos
class Producto(db.Model):
    idP = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), unique = True)
    precio = db.Column(db.Numeric(precision= 10,scale=2))
    imagen = db.Column(db.String(100))

class Cliente(db.Model):
    idC = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), unique = True)
    contraseña = db.Column(db.String(20), unique = True)
    email = db.Column(db.String(100))

class Venta(db.Model):
    idV = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime,default = datetime.utcnow)
    cliente_id = db.Column(db.ForeignKey('cliente.idC'))

class Detalle(db.Model):
    idD = db.Column(db.Integer, primary_key = True)
    producto_id = db.Column(db.ForeignKey('producto.idP'))
    venta_id = db.Column(db.ForeignKey('venta.idV'))
    cantidad = db.Column(db.Integer)