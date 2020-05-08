from flask import Flask,render_template,url_for,redirect,request,flash,abort
from flask_wtf import Form
from app.auth.forms import LoginForm,RegistrationForm,UpdateProfile,CommentForm,FeedBackForm,UpdatePic
from app import app,db,login_manager
from datetime import datetime
from flask_login import login_required,login_user,current_user,logout_user
from . import auth
from ..model import User,Role,Comment
from .. import db
from flask_bootstrap import Bootstrap
import secrets
import os
from sqlalchemy import desc

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


    


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
        bm = Role(title = title,review=review)
        
        db.session.add(bm)
        db.session.commit()
        
        return redirect(url_for('mainindex'))
    return render_template('add.html',form = form)


@app.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first_or_404()
    return render_template("profile.html", user = user)     



@app.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    update_form = UpdateProfile()
    user = User.query.filter_by(username = uname).first_or_404()
    if update_form.validate_on_submit():
        user.bio = update_form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('profile',uname=user.username))

    return render_template('user.html',update_form = update_form,user=user)


# @app.route('/user/updates',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename =save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
        
#         db.session.commit()
#     return redirect(url_for('profile',uname=uname))

def save_picture(form_picture):
    random_hex = secrets.toxen_hex(8)
    f_name.f_ext = os.path.splitext(form_picture.filename)
    picture_fn= random_hex + f_ext
    picture_path = os.path.join(app.root_path,'static/photos','picture_fn')
    return picture_fn

@app.route('/update_pic',methods = ['GET','POST'])
@login_required

def update_pic():
    sup_form = UpdatePic()
    user = User.query.filter_by(username = uname).first()
    if sup_form.validate_on_submit():
        if sup_form.picture.data:
            picture_file = save_picture(sup_form.picture.data)
            current_user.profile_pic_path = picture_file
        current_user.username = sup_form.username.data()
        current_user.email = sup_form.email.data()
        db.session.commit()
        flash('account update')
        return redirect(url_for('profile'))
        
    profile_pic_path = url_for('static', filename = 'app/static/photos' + current_user.profile_pic_path )
    return render_template('profile.html',profile_pic_path =profile_pic_path,sup_form = sup_form )


@app.route('/login',methods = ["GET","POST"])

def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        current_user = user
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

@app.route('/<int:cname>/comment',methods = ["GET","POST"])
def comment(cname):
    comments= FeedBackForm()
    # user = User.query.filter_by(username = uname).first_or_404()
    role=Role.query.filter_by(id=cname).first_or_404()  
    comment_query = Comment.query.filter_by(role_id = role.id).all()
    if comments.validate_on_submit():
        
        
        
        comment = Comment(comment= comments.comment.data,comment_id = comment.id,role_id = role.id,user_id = current_user.id)
        
        db.session.add(comment)
        db.session.commit()
        
        return redirect(url_for('mainindex',cname=cname))
    return render_template('comment.html',comment = comments,role=role,comments=comment_query)


@app.route('/logout')

def logout():
    logout_user()
    return redirect(url_for('mainindex'))


@app.errorhandler(404)

def error(e):
    return render_template('404.html'),404