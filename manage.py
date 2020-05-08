#! /usr/bin/env python

from app import app

from flask_script import Manager,prompt_bool
from app import db
from app.model import User,Role,Comment
from flask_migrate import Migrate,MigrateCommand
from flask_login import login_required,login_user,current_user

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)





@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Role = Role,Comment=Comment )

if __name__ == '__main__':
    db.init_app(app)
    manager.run()