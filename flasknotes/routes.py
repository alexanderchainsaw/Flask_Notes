from flask import render_template, redirect, request, url_for, flash, Blueprint
from .forms import LoginForm, RegistrationForm, NoteForm
from .models import User, Note
from . import db, bcrypt

view = Blueprint('main_routes', __name__)


@view.route('/', methods=['GET', 'POST'])
@view.route('/notes', methods=['GET', 'POST'])
def home():
    form = NoteForm()
    
    if form.validate_on_submit():
        new_note = Note(
            title=form.title.data,
            content=form.content.data,
            user_id=1,
        )
        db.session.add(new_note)
        db.session.commit()

        return redirect(url_for('main_routes.home'))

    return render_template('notes.html', form=form, data=Note.query.all(), count=Note.query.count())


@view.route('/<note_id>/delete', methods=['POST'])
def delete_note(note_id):
    data = Note.query.get_or_404(note_id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('main_routes.home'))


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