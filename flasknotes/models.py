from . import db
from sqlalchemy import func

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True)
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(20))
    register_date = db.Column(db.Date, server_default=func.now())
    notes = db.relationship('Note')
    
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # created_date = db.Column(db.Date, server_default=func.now())
    created_date = db.Column(db.Integer, default=1)
    title = db.Column(db.String(40))
    content = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))