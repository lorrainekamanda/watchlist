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
    comments = db.relationship('Comment',backref = 'user',lazy = 'dynamic')
    role = db.relationship('Role',backref = 'user',lazy = 'dynamic')
    bio = db.Column(db.String(255),unique = False)
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(215))

      
    
   

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
    comment = db.relationship('Comment',backref = 'role',lazy = 'dynamic')
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    
    @staticmethod
    def newest(num):
        return Role.query.order_by(desc(Role.date)).limit(num)
    
  
    
    
    
    def __repr__(self):
        return f'User {self.review} {self.title}'
    
    


  

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key=True) 
    comment = db.Column(db.String(300))
    date = db.Column(db.DateTime,default = datetime.utcnow) 
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'))


   

    

    @classmethod
    def new(cls,role_id):
         comment = Comment.query.filter_by(role_id = role_id).all()  

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.comment} '



        

