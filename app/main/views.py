from flask import render_template 
from . import main 
from .. import db,photos 


# Views
@main.route('/')
def index():

    return render_template('index.html')