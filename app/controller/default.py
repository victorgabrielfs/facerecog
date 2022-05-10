from app import app, db
from flask import render_template, request, redirect, url_for
from app.model.forms import LoginForm, SignUpForm
from app.model.tables import User


@app.route('/<user>')
@app.route('/', defaults={"user": None})
def helloworld(user):
    return render_template('index.html', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
        
    return render_template('signup.html', form=form)

