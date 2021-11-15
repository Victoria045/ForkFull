<<<<<<< HEAD
from flask import Flask,render_template,request,redirect,url_for
=======
from distutils.command.upload import upload
from flask import Flask,render_template,request,redirect,url_for,abort
>>>>>>> 89d5507 (View a single upload)
from . import main 
from .. import db,photos 
from .forms import UploadForm
from ..models import User,Upload
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

        # image_path = secure_filename(form.image_path.data.filename)
        # image_path = form.image_path.data 

        name = form.name.data
        category = form.category.data 
        price = form.price.data 
        new_upload_object = Upload(image_path=file_url,name=name, category=category, price=price)
        new_upload_object.save_upload()
        # import pdb; pdb.set_trace()
        return redirect(url_for('main.index')) 

<<<<<<< HEAD
    # else:
    #     file_url = None
    return render_template('upload.html', form=form) 
=======
    return render_template('upload.html', form=form)

@main.route('/uploads/<int:id>')
#@login_required
def uploads(id):
    upload = Upload.query.get(id)
    return render_template('single_upload.html',upload=upload)

@main.route('/uploads/<int:id>/update', methods=['GET', 'POST'])
#@login_required
def update_upload(id):
    upload = Upload.query.get(id)
    if upload is None:
        abort(404)
    # if upload.user != current_user:
    #     abort(403)
    form = UploadForm() 
    if form.validate_on_submit():
        # image = form.image.data 
        upload.name = form.name.data 
        upload.category = form.category.data 
        upload.price = form.price.data 
        db.session.commit()
        return redirect(url_for('main.index'))
    elif request.method == 'GET':
        form.name.data=upload.name
        form.category.data = upload.category
        form.price.data = upload.price
    title='Update Upload'
    return render_template('upload.html', title=title,form=form)
>>>>>>> 89d5507 (View a single upload)
