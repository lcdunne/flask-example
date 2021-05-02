from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, SubmitField, BooleanField)
from wtforms.validators import (
    InputRequired, Length, Email, EqualTo
)

class RegistrationForm(FlaskForm):

    email = StringField(
        'Email',
        validators=[InputRequired(),
                    Email()])

    username = StringField(
        'Username',
        validators=[InputRequired(),
                    Length(min=2, max=20)])

    password = PasswordField(
        'Password',
        validators=[InputRequired()])

    confirm_password = PasswordField(
        'Confirm Password',
        validators=[InputRequired(),
                    EqualTo('password')])

    submit = SubmitField('Register')

class LoginForm(FlaskForm):

    username = StringField(
        'Username',
        validators=[InputRequired(),
                    Length(min=2, max=20)])

    password = PasswordField(
        'Password',
        validators=[InputRequired()])

    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')
