from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True)
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(20))
    register_date = ... # date when joined
    notes = db.relationship('Note')
    
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # date
    title = db.Column(db.String(40))
    content = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))