from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo
from app.model import User
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed
from wtforms.fields.html5 import EmailField
from wtforms.widgets import TextArea
from flask_login import login_required,login_user,current_user






class LoginForm(FlaskForm):
    
    email = EmailField('Your Email Address',validators =[DataRequired()])
    password = PasswordField('Password',validators =[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class FeedBackForm(FlaskForm):
    
    comment = TextAreaField('Pitch Idea',validators =[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    title = StringField('pitch Header title')
    review = TextAreaField('Pitch Idea')
    submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
    email = EmailField('Your Email Address')
    username = StringField('Username',validators = [DataRequired()])
    password = PasswordField('Password',validators = [DataRequired()])
    remember_me = BooleanField('logged in')
    submit = SubmitField('Log In')
    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Username already taken')    

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class UpdatePic(FlaskForm):
    username = StringField('Update Username',validators = [DataRequired()])
    email = EmailField('Update Email Address',validators =[DataRequired()])
    picture = FileField('update profile')
    submit = SubmitField('Submit')

    def validate_username(self,username):
        if username.data != current_user.data:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError('There is an account with that Username')

    def validate_email(self,email):
        if email.data != current_user.data:
           user = User.query.filter_by(email = email.data).first()
           if user: 
                raise ValidationError('Email already taken')   