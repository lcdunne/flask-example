from flask import (
    render_template,
    redirect, url_for, flash)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash)
from app import db
from . import main_bp
from app.models import User
from .forms import RegistrationForm, LoginForm


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/registration', methods=['GET', 'POST'])
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

        return redirect(url_for('main.login'))
    return render_template('registration.html', title='Register', form=form)


@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    n_attempts = 3

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            to_check = user.password_hash
            if check_password_hash(to_check, form.password.data):
                n_attempts = 3
                return redirect(url_for('main.home'))
            else:
                n_attempts -= 1
                flash(f'Invalid credentials - {n_attempts} attempts left.')
                return redirect(url_for('main.login'))
    return render_template('login.html', title='Log In', form=form)


@main_bp.route('/home')
def home():
    return "Logged in"
