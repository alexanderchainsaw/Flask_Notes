from flask import render_template, redirect, request, url_for, flash, Blueprint

view = Blueprint('main_routes', __name__)

@view.route('/')
def home():
    return render_template('notes.html')