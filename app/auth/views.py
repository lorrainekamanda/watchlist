from flask import Flask,render_template,url_for,redirect,request,flash
from flask_wtf import Form
from app.auth.forms import LoginForm,RegistrationForm,UpdateProfile,CommentForm

from app import app,db,login_manager
from datetime import datetime
from flask_login import login_required,login_user,current_user,logout_user
from . import auth
from ..model import User,Role
from .. import db
from flask_bootstrap import Bootstrap

  



@app.route('/index')
@app.route('/')

def mainindex():
 
    return render_template('index.html',new_bookmarks = Role.newest(5))
     




@app.route('/add', methods = ["POST","GET"])

@login_required
def add():
    form = CommentForm()
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        bm = Role(user = current_user,title = title,review=review)
        db.session.add(bm)
        db.session.commit()
        
        return redirect(url_for('mainindex'))
    return render_template('add.html',form = form)

@app.route('/user/<name>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    
    user = User.query.filter_by(username = name).first_or_404()
    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',name=user.username))

    return render_template('profile/update.html',form =form)





    
@login_required
@app.route('/user/<uname>')

def user(uname):

    user = User.query.filter_by(username = uname).first_or_404()

    return render_template('user.html',user = user)


@app.route('/login',methods = ["GET","POST"])

def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember_me.data)
            flash("welcome {} You have sucessfully logged in ".format(user.email))
            return redirect(request.args.get('next') or url_for('mainindex'))
        flash('Opps check again incorrect username or password')
    return render_template('login.html',login_form=login_form)



@app.route('/signup',methods = ["GET","POST"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('login'))
        
    return render_template('signup.html',registration_form = form)




@app.route('/logout')

def logout():
    logout_user()
    return redirect(url_for('mainindex'))


@app.errorhandler(404)

def error(e):
    return render_template('404.html'),404