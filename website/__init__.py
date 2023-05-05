# import os
from flask import Flask
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager

app = Flask(__name__)

# # database setup
# app.config['SECRET_KEY'] = "mysecretkey"
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
# Migrate(app, db)

# # setup login
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "users.login"

from . core.views import core
app.register_blueprint(core)