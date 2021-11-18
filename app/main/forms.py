from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField,IntegerField,SelectField,TextAreaField,SubmitField 
from wtforms.validators import DataRequired 

class UploadForm(FlaskForm):
    image_path = FileField('Select picture upload', validators=[FileAllowed(['jpeg', 'png'])])
    name = StringField('Enter Food Name', validators=[DataRequired()]) 
    category = SelectField('Category', choices=[('BreakFast','BreakFast'), ('Lunch','Lunch'),('Dinner','Dinner')])
    price = IntegerField('Price', validators=[DataRequired()]) 
    submit = SubmitField('Upload')
    
class Authentication(FlaskForm):
    role = SelectField('Post category',choices=[('Owner','Owner'),('Customer', '')], validators=[DataRequired()])
    submit = SubmitField('Submit')