from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo
from app.model import User
from wtforms import ValidationError

from wtforms.fields.html5 import EmailField
from wtforms.widgets import TextArea
from flask_login import login_required,login_user


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    
    email = EmailField('Your Email Address',validators =[DataRequired()])
    password = PasswordField('Password',validators =[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

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

