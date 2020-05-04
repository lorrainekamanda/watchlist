import os
from .config import DevConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import login_required,login_user,current_user
from flask_bootstrap import Bootstrap
from flask_mail import Mail,Message



app = Flask(__name__,instance_relative_config = True)


app.config.from_object(DevConfig)
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.init_app(app)

mail = Mail(app)
mail.init_app(app)
db.init_app(app)

app.config['SECRET_KEY'] = '\xae~\x05?4\xe8\x1a\xf0v}\x9f\xf3<H\xefu4\x8e\xbf{c\xe5\x9d\x7f'
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://lorrainekamanda:leilas@localhost/watchlists'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'lorrainekamanda@gmail.com'  
app.config["MAIL_PASSWORD"] = 'leilanjeri123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_PORT_TLS'] = 587
mail = Mail(app)
mail.init_app(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'lorrainekamanda@gmail.com', recipients = ['lorrainekamanda@gmail.com'])
   msg.body = "Hello and Welcome"
   mail.send(msg)
  


def create_app(config_name):
    app = Flask(__name__)
   
    Bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    bootstrap.init_app(app)
    mail.init_app(app)
    
    return app

from app import models
from app.auth import views