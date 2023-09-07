from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class ClientForm():
        nombre = StringField('ingrese nombre:' , 
                         validators=[InputRequired(message="Nombre requerido")])
    
        contraseña = StringField("ingrese contraseña:" ,
                          validators=[InputRequired(message="Contraseña requerida")])
    
        email = StringField("ingrese correo electronico:" ,
                          validators=[InputRequired(message="Email invalido")])

class NewClientForm(FlaskForm, ClientForm):
    submit = SubmitField("Registrar")
    
class EditClientForm(FlaskForm,ClientForm):
    submit = SubmitField("Registrar")