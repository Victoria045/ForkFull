from flask import Flask
from flask_bootstrap import Bootstrap 
from config import config_options 
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.exc import IntegrityError
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class 
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os

basedir = os.path.abspath(os.path.dirname(__file__)) 

bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES) 

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/photos')

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)  

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint) 

    # configure UploadSet
    configure_uploads(app,photos)
    
    # set maximum file size, default is 16M 
    patch_request_class(app) 

    return app 