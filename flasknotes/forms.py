from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import email_validator
from wtforms.widgets import TextArea
from .models import User


class RegistrationForm(FlaskForm):

    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Account')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('Username taken')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Account under this email already exists')


class LoginForm(FlaskForm):

    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    # def validate_email(self, email):
    #     if not User.query.filter_by(email=email.data).first():
    #         raise ValidationError('Invalid email')
    #
    # def validate_password(self, password):
    #     if bcrypt.check_password_hash(password, password.data)
    #         raise ValidationError('Invalid email')


class NoteForm(FlaskForm):
    title = StringField('Title',
                        validators=[DataRequired()])
    content = StringField('Content',
                          validators=[DataRequired()],
                          widget=TextArea())

    submit = SubmitField('Create Note')