from enum import unique
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

SECRET_KEY = '6\xf4X\x1e\xb6\xc2>\xac\x92\x85\x01\xcb\xfe\xc4T\xae'#os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
#import routes
from market import routes