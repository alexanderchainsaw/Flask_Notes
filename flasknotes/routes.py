from flask import render_template, redirect, request, url_for, flash, Blueprint
from forms import LoginForm, RegistrationForm
from models import User, Note
from . import db, bcrypt

view = Blueprint('main_routes', __name__)


@view.route('/')
def home():
    return render_template('notes.html')


@view.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"You are now logged in as {form.username.data}")
        return redirect(url_for('main_routes.home'))
    return render_template('login.html', form=form)


@view.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():



        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )


        flash(f"Account created for {form.username.data}!", category='success')
        return redirect(url_for('main_routes.home'))
    return render_template('register.html', form=form)