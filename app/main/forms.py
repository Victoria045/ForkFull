from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed 
from wtforms import StringField,IntegerField,SelectField,TextAreaField,SubmitField 
from wtforms.validators import Required 

class UploadForm(FlaskForm):
    picture = FileField('Select picture upload', validators=[FileAllowed('jpg','png')])
    name = StringField('Enter Restaurant Name', validators=[Required()]) 
    category = SelectField('Category', choices=[('BreakFast','BreakFast'), ('Lunch','Lunch'),('Diner','Diner')])
    price = IntegerField('Price', validators=[Required()]) 
    submit = SubmitField('Upload')