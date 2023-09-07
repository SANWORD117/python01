from . import productos_bp
from flask import render_template, redirect, flash
from .forms import NewProductForm, EditProductForm
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
        flash("Producto registrado exitosamente")
        return redirect('/productos/listar')
    return render_template('new.html', form = form)

@productos_bp.route('/listar' )
def listar():
    productos= app.Producto.query.all()
    return render_template('listar.html' ,
                           productos=productos)
    
@productos_bp.route('/editar/<idP>' ,
                    methods=['GET','POST'])
def editar(idP):
    #seleccionar el producto
    #con el id
    p= app.models.Producto.query.get(idP)
    #cargo el formulario
    #con los atributos de producto
    form_edit = EditProductForm(obj = p)
    if form_edit.validate_on_submit():
        form_edit.populate_obj(p)
        app.db.session.commit()
        flash("Producto editado exitosamente")
        return redirect("/productos/listar")
    return render_template('new.html',
                        form=form_edit)
    
@productos_bp.route('/eliminar/<idP>' ,
                    methods=['GET','POST'])
def eliminar(idP):
    #seleccionar el producto
    #con el id
    p= app.models.Producto.query.get(idP)
    #eliminar el producto
    app.db.session.delete(p)
    app.db.session.commit()
    flash("Producto funado exitosamente")
    return redirect("/productos/listar")