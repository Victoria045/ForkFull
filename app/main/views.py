from flask import Flask,render_template,request, session,redirect,url_for
from . import main 
from .. import db,photos 
from .forms import UploadForm
from ..models import User,Upload,ProductOrder,Cart
from werkzeug.utils import secure_filename
import os 


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

    # import pdb; pdb.set_trace();

    form = UploadForm()
    if form.validate_on_submit():
        filename = photos.save(form.image_path.data)
        file_url = photos.url(filename)

        name = form.name.data
        category = form.category.data 
        price = form.price.data 
        new_upload_object = Upload(image_path=file_url,name=name, category=category, price=price)
        new_upload_object.save_upload()
        # import pdb; pdb.set_trace()
        return redirect(url_for('main.index')) 

    # else:
    #     file_url = None
    return render_template('upload.html', form=form)


@main.route('/add_cart', methods = ['POST','GET'])
# @login_required 
def add_cart():
    upload_id = request.form.get('upload.id')
    quantity = request.form.get('quantity')
    all_uploads = ProductOrder.query.filter_by(upload_id = upload_id).all()
    new_upload = ProductOrder(upload_id=upload_id)
    new_upload.save_productorder()
    

    # return redirect(url_for('main.cart'))
    return render_template('cart.html', quantity=quantity, upload_id=upload_id)
