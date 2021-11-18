from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField,IntegerField,SelectField,TextAreaField,SubmitField, FileField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.validators import DataRequired 
from flask_login import  current_user

class UploadForm(FlaskForm):
    image_path = FileField('Select picture upload', validators=[FileAllowed(['jpeg', 'png'])])
    name = StringField('Enter Food Name', validators=[DataRequired()]) 
    category = SelectField('Category', choices=[('BreakFast','BreakFast'), ('Lunch','Lunch'),('Dinner','Dinner')])
    price = IntegerField('Price', validators=[DataRequired()]) 
    submit = SubmitField('Upload')

class accountForm(FlaskForm):
    picture = FileField('Choose Profile picture', validators=[
                        FileAllowed(['jpg', 'png', 'jpeg'])])
    restaurant_name = StringField('Restaurant name', validators=[DataRequired()]
    )   
    location = StringField('Location', validators=[DataRequired()]) 

    submit = SubmitField('Submit')

# class updateAccount(FlaskForm):      

class Authentication(FlaskForm):
    role = SelectField('Post category',choices=[('Owner','Owner'),('Customer', '')], validators=[DataRequired()])
    submit = SubmitField('Submit')