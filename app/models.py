from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime 
import os

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    __tablename__ = 'users' 

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    uploads = db.relationship('Upload', backref='user', lazy='dynamic')  

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

# @login_manager.user_loader
# def load_user(owner_id):
#     return Owner.query.get(int(owner_id))

# class Owner(db.Model,UserMixin):
#     __tablename__ = 'owners'

#     id = db.Column(db.Integer,primary_key = True)
#     username = db.Column(db.String(255),index = True)
#     email = db.Column(db.String(255),unique = True,index = True)
#     password_hash = db.Column(db.String(255))
#     pass_secure = db.Column(db.String(255))
    
#     @property
#     def password(self):
#         raise AttributeError('You cannot read the password attribute')

#     @password.setter
#     def password(self, password):
#         self.pass_secure = generate_password_hash(password)


#     def verify_password(self,password):
#         return check_password_hash(self.pass_secure,password)

#     def __repr__(self):
#         return f'User {self.username}'


class Upload(db.Model): 
    __tablename__ = 'uploads' 

    id = db.Column(db.Integer, primary_key = True) 
    image_path = db.Column(db.Text, nullable = False, default='default.jpeg') 
    name = db.Column(db.String(255),nullable = False) 
    category = db.Column(db.String(255), index = True,nullable = False) 
    price = db.Column(db.Integer, index = True,nullable = False) 
    time_posted = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 

    def save_upload(self):
        db.session.add(self)
        db.session.commit() 

    # def __repr__(self):
    #     return f'Upload {#{self.post}#}' 

class Account(db.Model):
    _tablename_ = 'account'
    id = db.Column(db.Integer, primary_key = True) 
    picture = db.Column(db.Text, nullable = False)
    restaurant_name = db.Column(db.String(255),nullable = False) 
    location = db.Column(db.String(255),nullable = False)

    def save_account(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"Account('{self.picture}', '{self.restaurant_name}', '{self.location}')"

    
    # def __repr__(Self):
    #     return f'Upload {#{self.post}#}' 