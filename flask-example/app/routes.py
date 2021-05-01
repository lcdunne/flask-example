from flask import render_template, redirect, url_for, flash
from app import app, db
from app.forms import RegistrationForm, LoginForm
from app.models import User
from werkzeug.security import (
    generate_password_hash,
    check_password_hash)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        # Check if the user already exists
        email = form.email.data

        user = User.query.filter_by(email=email).first()

        if user is None:
            user = User(
                username=form.username.data,
                password_hash=generate_password_hash(form.password.data),
                email=form.email.data)
            db.session.add(user)
            db.session.commit()

        else:
            flash("Already exists. Log in instead.")

        return redirect(url_for('login'))
    return render_template('registration.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    n_attempts = 3

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            to_check = user.password_hash
            if check_password_hash(to_check, form.password.data):
                n_attempts = 3
                return redirect(url_for('home'))
            else:
                n_attempts -= 1
                flash(f'Invalid credentials - {n_attempts} attempts left.')
                return redirect(url_for('login'))
    return render_template('login.html', title='Log In', form=form)


@app.route('/home')
def home():
    return "Logged in"
