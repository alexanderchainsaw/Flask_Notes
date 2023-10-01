from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'asdasddadaddasadsdfgsfgvcvbbvccbvctreyhjkk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_notes.db'

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

db.init_app(app)

from .routes import view

app.register_blueprint(view, url_prefix='/')

from .models import User, Note

with app.app_context():
    db.create_all()
        
