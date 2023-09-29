from flask import render_template, redirect, request, url_for, flash, Blueprint
from .forms import LoginForm, RegistrationForm, NoteForm
from .models import User, Note
from . import db, bcrypt
from flask_login import login_user, current_user, logout_user

view = Blueprint('main_routes', __name__)


@view.route('/', methods=['GET', 'POST'])
@view.route('/notes', methods=['GET', 'POST'])
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('main_routes.login'))
    form = NoteForm()
    if form.validate_on_submit():
        new_note = Note(
            title=form.title.data,
            content=form.content.data,
            user_id=current_user.id,
        )
        db.session.add(new_note)
        db.session.commit()

        return redirect(url_for('main_routes.home'))

    return render_template('notes.html', form=form)


@view.route('/<note_id>/delete', methods=['POST'])
def delete_note(note_id):
    data = Note.query.get_or_404(note_id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('main_routes.home'))


@view.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main_routes.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f'Welcome back, {user.username}!', category='success')
            return redirect(url_for('main_routes.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', category='danger')

    return render_template('login.html', form=form)


@view.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main_routes.home'))
    form = RegistrationForm()
    if form.validate_on_submit():

        db.session.add(
            User(
            username=form.username.data,
            email=form.email.data,
            password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            )
        )
        db.session.commit()

        flash(f'Account created for {form.username.data}', category='success')
        return redirect(url_for('main_routes.login'))
    return render_template('register.html', form=form)

@view.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main_routes.home'))