from flask import Blueprint

#Crear y configurar el Blueprint
mi_blueprint = Blueprint('mi_blueprint',__name__, url_prefix= '/ejemplo')

#crear ruta del blueprint
@mi_blueprint.route('/saludo')
def saludo():
    return 'Si a todo'