from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,PasswordField,SubmitField,ValidationError,BooleanField
from wtforms.validators import Email, EqualTo,Required
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[Required(),Email()])
    username = StringField('Username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Password',validators = [Required()])
    Role = SelectField('Role', choices=[('customer','customer'), ('owner','owner')])
    submit = SubmitField('Register')
    
    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email!!')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken!!')
        
class LoginForm(FlaskForm):
    email = StringField('Email',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log In')