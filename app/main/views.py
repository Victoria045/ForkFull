from flask import Flask,render_template,request,redirect,url_for
from . import main 
from .. import db
from flask_login import login_required
from .forms import UploadForm, Authentication
import os 


# Views
@main.route('/')
def index():


    return render_template('index.html') 


@main.route('/new_upload', methods = ['POST','GET'])
# @login_required 
def new_upload():

    # import pdb; pdb.set_trace();

    form = UploadForm()
    if form.validate_on_submit():

        # image_path = secure_filename(form.image_path.data.filename)
        # image_path = form.image_path.data 

        # import pdb; pdb.set_trace()
        return redirect(url_for('main.index')) 

    # else:
    #     file_url = None
    return render_template('upload.html') 


    
