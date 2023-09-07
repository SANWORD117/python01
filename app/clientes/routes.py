from . import clientes_bp
from flask import render_template, redirect, flash
from .forms import NewClientForm, EditClientForm
import app
    
# #crear las rutas del blueprint
@clientes_bp.route('/crear', methods=["GET", "POST"])

def crear():
    p= app.models.Cliente()
    form2 = NewClientForm()
    if form2.validate_on_submit():
        # el formulario va a llenar 
        #el nuevo objeto producto por nosotros 
        form2.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        
        #Este metodo getcwd() permite identificar la ruta absoluta del proyecto
        #return os.getcwd()
        flash("Cliente registrado exitosamente")
        return redirect('/clientes/listar')
    return render_template('newC.html', form = form2)

@clientes_bp.route('/listar' )
def listar():
    clientes= app.Cliente.query.all()
    return render_template('listarC.html' ,
                           clientes=clientes)
    
@clientes_bp.route('/editar/<idC>' ,
                    methods=['GET','POST'])
def editar(idC):
    #seleccionar el producto
    #con el id
    p= app.models.Cliente.query.get(idC)
    #cargo el formulario
    #con los atributos de producto
    form_edit = EditClientForm(obj = p)
    if form_edit.validate_on_submit():
        form_edit.populate_obj(p)
        app.db.session.commit()
        flash("Cliente editado exitosamente")
        return redirect("/clientes/listar")
    return render_template('newC.html',
                        form=form_edit)
    
@clientes_bp.route('/eliminar/<idC>' ,
                    methods=['GET','POST'])
def eliminar(idC):
    #seleccionar el producto
    #con el id
    p= app.models.Cliente.query.get(idC)
    #eliminar el producto
    app.db.session.delete(p)
    app.db.session.commit()
    flash("Cliente funado exitosamente")
    return redirect("/clientes/listar")