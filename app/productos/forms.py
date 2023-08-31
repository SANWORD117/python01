from flask_wtf import FlaskForm
from wtforms import StringField , IntegerField, SubmitField
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileField, FileRequired, FileAllowed

class NewProductForm(FlaskForm):
    nombre = StringField('ingrese producto:' , 
                         validators=[InputRequired(message="Nombre requerido")])
    
    precio = IntegerField("ingrese precio:" ,
                          validators=[InputRequired(message="Precio requerido"),
                                      NumberRange(message="Precio fuera de rango",
                                                  min=10000 ,
                                                  max=100000)])
    
    imagen = FileField(validators=[FileRequired(message="Imagen requerida") ,
                                   FileAllowed(['jpg','png'] ,
                                               message="Solo se admiten imagenes")] , 
                       label="No se ingreso una vista previa del producto: ")
    
    submit = SubmitField("Registrar")