from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdasddadaddasadsdfgsfgvcvbbvccbvctreyhjkk'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_notes.db'
    db.init_app(app)
    
    from .routes import view
    
    app.register_blueprint(view, url_prefix='/')
    
    from .models import User, Note
    
    with app.app_context():
        db.create_all()
        
    return app