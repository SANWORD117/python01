from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from flask_bootstrap import Bootstrap
#blueprint
from .my_blueprint import mi_blueprint
from app.productos import productos_bp
from app.clientes import clientes_bp


#creacion y configuracion de la app
app = Flask(__name__)
app.config.from_object(Config)
Bootstrap = Bootstrap(app)

#registro de bluieprints
app.register_blueprint(mi_blueprint)
app.register_blueprint(productos_bp)
app.register_blueprint(clientes_bp)

# bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app,
                  db)

from .models import Producto, Cliente, Venta, Detalle

@app.route('/prueba')
def prueba():
    return render_template("prueba.html")