from . import db 
from datetime import datetime 

class User(db.Model):
    __tablename__ = 'users' 

    id = db.Column(db.Integer,primary_key = True)
    uploads = db.relationship('Upload', backref='user', lazy='dynamic')  


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
    #     return f'Upload {#{self.name}#}' 

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




    
    def __repr__(Self):
        return f'Upload {self.post}' 
