from flask import Flask,session,render_template,request,redirect,url_for,flash, abort
from flask_login import  current_user, login_required
from distutils.command.upload import upload
from urllib.parse import urlparse
from . import main 
from .. import db,photos 
from .forms import UploadForm, accountForm
from ..models import Account, User,Upload
from werkzeug.utils import secure_filename
from flask import send_from_directory
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
@login_required 
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
        return redirect(url_for('main.index')) 

    return render_template('upload.html', form=form) 


@main.route('/account/new', methods=['POST','GET']) 
@login_required
def account_new():
    form = accountForm()
    #import pdb; pdb.set_trace();
    if form.validate_on_submit():
        filename = photos.save(form.picture.data)
        file_url = photos.url(filename)
        restaurant_name = form.restaurant_name.data
        location = form.location.data 
        new_account_object = Account(picture=file_url,restaurant_name=restaurant_name, location=location)
        new_account_object.save_account()
        # account = Account.query.filter_by (id=new_account_object.id).first()
        # print(new_account_object)
        flash('Your info has been captured!', 'success')
        return redirect(url_for('main.account', id=new_account_object.id)) 

    return render_template('new_account.html', form=form)

@main.route('/account/<int:id>')
@login_required 
def account(id):
    
    account = Account.query.get(id) 
    print(account)
    
    return render_template('account.html', account=account)

@main.route('/account/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_account(id):
    account = Account.query.get(id)
    print(account)
    if account is None:
        abort(404)
    # if account.user != current_user:
    #     abort(403)
    form = accountForm()
    if form.validate_on_submit():
        filename = photos.save(form.picture.data)
        file_url = photos.url(filename)
        account.picture = file_url
        account.restaurant_name = form.restaurant_name.data
        account.location = form.location.data
        db.session.commit()
        return redirect(url_for('main.index'))
    elif request.method == 'GET':
        form = accountForm(request.form)
        url = account.picture
        get_image = urlparse(url)
        form.picture.data = os.path.basename(get_image.path)
        form.restaurant_name.data=account.restaurant_name
        form.location.data = account.location
        
    title='Update account'
    return render_template('new_account.html', form=form)
  
@main.route('/account/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_account(id):
    account = Account.query.get(id)
    if account is None:
        abort(404)
    # if account.user != current_user:
    #     abort(403)
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('.index'))

    # return render_template('upload.html', form=form)

@main.route('/uploads/<int:id>')
@login_required
def uploads(id):
    upload = Upload.query.get(id)
    return render_template('single_upload.html',upload=upload)

@main.route('/uploads/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update_upload(id):
    upload = Upload.query.get(id)
    if upload is None:
        abort(404)
    # if upload.user != current_user:
    #     abort(403)
    form = UploadForm() 
    if form.validate_on_submit():
        filename = photos.save(form.image_path.data)
        file_url = photos.url(filename)
        upload.image_path = file_url
        upload.name = form.name.data 
        upload.category = form.category.data 
        upload.price = form.price.data 
        db.session.commit()
        return redirect(url_for('main.index'))
    elif request.method == 'GET':
        form = UploadForm(request.form)
        url = upload.image_path
        get_image = urlparse(url)
        form.image_path.data = os.path.basename(get_image.path)
        form.name.data=upload.name
        form.category.data = upload.category
        form.price.data = upload.price
        print(form.image_path.data)

    title='Update Upload'
    return render_template('upload.html', title=title,form=form)

@main.route('/uploads/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete_upload(id):
    upload = Upload.query.get(id)
    if upload is None:
        abort(404)
    # if upload.user != current_user:
    #     abort(403)
    db.session.delete(upload)
   
    db.session.commit()
 
    return redirect(url_for('.index'))
    return render_template('upload.html', form=form) 