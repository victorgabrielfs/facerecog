from app import app
from flask import render_template
from app.model.forms import LoginForm, SignUpForm


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
    return render_template('signup.html', form=form)

