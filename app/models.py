from . import db 
from datetime import datetime 

class User(db.Model):
    __tablename__ = 'users' 

    id = db.Column(db.Integer,primary_key = True)
    uploads = db.relationship('Upload', backref='user', lazy='dynamic') 
    productorder = db.relationship('ProductOrder', backref='user', lazy='dynamic')

class Upload(db.Model): 
    __tablename__ = 'uploads' 

    id = db.Column(db.Integer, primary_key = True) 
    image_path = db.Column(db.Text, nullable = False, default='default.jpeg') 
    name = db.Column(db.String(255),nullable = False) 
    category = db.Column(db.String(255), index = True,nullable = False) 
    price = db.Column(db.Integer, index = True,nullable = False) 
    time_posted = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    productorder = db.relationship('ProductOrder', backref='upload', lazy='dynamic')

    def save_upload(self):
        db.session.add(self)
        db.session.commit() 

    def __repr__(self):
        return f'Upload {self.post}' 

    
# class Order(db.Model): 
#     __tablename__ = 'order' 

#     id = db.Column(db.Integer, primary_key = True) 
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     carts = db.relationship('Cart', backref='order', lazy='dynamic')
#     upload_id = db.Column(db.Integer, db.ForeignKey('uploads.id'))

#     def save_order(self):
#         db.session.add(self)
#         db.session.commit()
    
#     def __repr__(Self):
#         return f'order {#{self.order}#}'

# class Cart(db.Model): 
#     __tablename__ = 'carts' 

#     id = db.Column(db.Integer, primary_key = True) 
#     quantity = db.Column(db.Integer, index = True,nullable = False) 
#     upload_id = db.Column(db.Integer, db.ForeignKey('uploads.id'))
#     order_id = db.Column(db.Integer, db.ForeignKey('order.id'))

#     def save_order(self):
#         db.session.add(self)
#         db.session.commit()
    
#     def __repr__(Self):
#         return f'cart {#{self.cart}#}'


class Cart(db.Model): 
    __tablename__ = 'carts' 

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    productorder = db.relationship('ProductOrder', backref='cart', lazy='dynamic')

    def save_order(self):
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self):
        return f'cart {self.cart}'
class ProductOrder(db.Model): 
    __tablename__ = 'productorder' 

    id = db.Column(db.Integer, primary_key = True) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'))
    upload_id = db.Column(db.Integer, db.ForeignKey('uploads.id'))
    quantity = db.Column(db.Integer, index = True)

    def save_productorder(self):
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self):
        return f'ProductOrder {self.upload_id}'
    