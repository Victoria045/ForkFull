from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap 
from config import config_options 
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.exc import IntegrityError
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class 
from flask_mail import Mail 
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os

basedir = os.path.abspath(os.path.dirname(__file__)) 

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES) 
mail = Mail()

def create_app(config_name):

    app = Flask(__name__)
~
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/photos')

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app) 
    login_manager.init_app(app) 
    mail.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint) 

    # Registering the auth bluprints
    from . auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/user-account')
    
    # configure UploadSet
    configure_uploads(app,photos)
    
    # set maximum file size, default is 16M 
    patch_request_class(app) 

    return app 