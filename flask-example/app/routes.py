from flask import render_template, redirect, url_for
from app import app
from app.forms import RegistrationForm, LoginForm


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        return redirect(url_for('login'))
    return render_template('registration.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        print("OK")
        return redirect(url_for('home'))
    return render_template('login.html', title='Log In', form=form)


@app.route('/home')
def home():
    return "Logged in"
