from . import productos_bp
from flask import render_template
from .forms import NewProductForm
import app
import os
    
# #crear las rutas del blueprint
@productos_bp.route('/crear', methods=["GET", "POST"])

def crear():
    p= app.models.Producto()
    form = NewProductForm()
    if form.validate_on_submit():
        # el formulario va a llenar 
        #el nuevo objeto producto por nosotros 
        form.populate_obj(p)
        p.imagen = form.imagen.data.filename
        app.db.session.add(p)
        app.db.session.commit()
        #ubicar el archivo de imagen en la carpeta app/productos/imagenes
        file = form.imagen.data
        file.save(os.path.abspath(os.getcwd() + '/app/productos/imagenes/' + p.imagen))
        
        #Este metodo getcwd() permite identificar la ruta absoluta del proyecto
        #return os.getcwd()
        return 'producto registrado'
    return render_template('new.html', form = form)

@productos_bp.route('/listar' )
def listar():
    productos= app.Producto.query.all()
    return render_template('listar.html' ,
                           productos=productos)