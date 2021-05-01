from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import (
    InputRequired, Length, Email, EqualTo
)

class RegistrationForm(FlaskForm):

    email = StringField(
        'email_label',
        validators=[InputRequired(),
                    Email()])

    username = StringField(
        'username_label',
        validators=[InputRequired(),
                    Length(min=2, max=20)])

    password = PasswordField(
        'password_label',
        validators=[InputRequired()])

    confirm_password = PasswordField(
        'confirm_password_label',
        validators=[InputRequired(),
                    EqualTo('password')])

    submit = SubmitField('Register')

class LoginForm(FlaskForm):

    username = StringField(
        'username_label',
        validators=[InputRequired(),
                    Length(min=2, max=20)])

    password = PasswordField(
        'password_label',
        validators=[InputRequired()])

    submit = SubmitField('Login')
