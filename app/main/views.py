from flask import Flask,render_template,request,redirect,url_for
from . import main 
from .. import db,photos 
from .forms import UploadForm
from ..models import User,Upload


# Views
@main.route('/')
def index():

    uploads = Upload.query.all()
    breakfast = Upload.query.filter_by(category = 'BreakFast').all()
    lunch = Upload.query.filter_by(category = 'Lunch').all()
    dinner = Upload.query.filter_by(category = 'Dinner').all()
    return render_template('index.html', uploads = uploads, breakfast = breakfast, lunch = lunch, dinner = dinner) 


@main.route('/new_upload', methods = ['POST','GET'])
# @login_required 
def new_upload():

    form = UploadForm() 
    if form.validate_on_submit():
        # image = form.image.data 
        name = form.name.data 
        category = form.category.data 
        price = form.price.data 
        new_upload_object = Upload(name=name, category=category, price=price)
        new_upload_object.save_upload()
        return redirect(url_for('main.index')) 

    return render_template('upload.html', form=form)