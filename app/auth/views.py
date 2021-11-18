from flask import render_template,redirect,url_for,request,flash
from . import auth
from ..models import User
from .forms import RegistrationForm,LoginForm,RegistrationFormOwner,LoginFormOwner
from .. import db
from flask_login import login_user,logout_user,login_required
from .forms import RegistrationForm
from .. import db



@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
    
        flash('You have created your account successfully')
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/registration.html',registration_form = form)


@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid Email or Password')

    title = "ForkFull login"
    return render_template('auth/login.html',login_form = login_form,title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for("main.index"))

# @auth.route('/registerOwner',methods = ["GET","POST"])
# def registerOwner():
#     form = RegistrationFormOwner()
#     if form.validate_on_submit():
#         user = User(email = form.email.data, username = form.username.data,password = form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('You have created your account successfully')
#         return redirect(url_for('auth.login'))
#         title = "New Account"
#     return render_template('auth/registrationOwner.html',registration_form = form)


# @auth.route('/loginOwner',methods=['GET','POST'])
# def loginOwner():
#     login_form = LoginFormOwner()
#     if login_form.validate_on_submit():
#         user = User.query.filter_by(email = login_form.email.data).first()
#         if user is not None and user.verify_password(login_form.password.data):
#             login_user(user,login_form.remember.data)
#             return redirect(request.args.get('next') or url_for('main.index'))

#         flash('Invalid Email or Password')

#     title = "Owner login"
#     return render_template('auth/loginOwner.html',login_form = login_form,title=title)

# @auth.route('/logoutOwner')
# @login_required
# def logoutOwner():
#     logout_user()
#     flash('You have been logged out')
#     return redirect(url_for("main.index"))

# @auth.route('/customer')
# def customer():
#     return render_template("auth/customer.html")