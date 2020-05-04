from datetime import datetime
from sqlalchemy import desc
from . import db
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_required,login_user
from flask_security import current_user
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model,UserMixin):

    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(100),unique = True)
    email = db.Column(db.String(100),unique = True)
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'))
    bio = db.Column(db.String(255),unique = False)
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
   

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

class Role (db.Model):

    __tablename__ = 'role'

    id = db.Column(db.Integer,primary_key=True) 
    title = db.Column(db.String(400))
    date = db.Column(db.DateTime,default = datetime.utcnow)
    review = db.Column(db.String(300))
    bookmarks = db.relationship('User',backref = 'role',lazy = 'dynamic')
    
    @staticmethod
    def newest(num):
        return Role.query.order_by(desc(Role.date)).limit(num)   

    def __repr__(self):
        return f'User {self.title} {self.review} '



        
# class UserMixin(object):
#     def is_active(self):
#         return True
#     def is_authenticated(self):
#         return True
#     def is_anonymous(self):
#         return False
#     def get_id(self):
#         try:
#             return unicode (self.id)
#         except AttributeError:
#             raise NotImplementedError('No id ')
#     def __eq__(self,other):
#         if isinstance(other,UserMixin):
#             return self.get_id()==other.get_id()
#         return NotImplemented
          
#     def __ne__(self,other):
#         equal = self.__eq__(other)
#         if equal is NotImplemented:
#             return NotImplemented
#         return not equal

# class AnonymousUserMixin(object):
#     def is_authenticated(self):
#         return False
#     def is_active(self):
#         return False
#     def is_anonymous(self):
#         return True
#     def get_id(self):
#         get_id