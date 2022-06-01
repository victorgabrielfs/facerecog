from app import app, db
from flask import render_template, redirect, url_for, flash, Response, request, jsonify

from app.controller.recog.recog_utils import gen, VideoCamera
from app.model.forms import LoginForm, SignUpForm
from app.model.tables import User, bcrypt, Images
from flask_login import login_user, logout_user, login_required
from werkzeug.utils import secure_filename


@app.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.username.data).first()

        if user and user.verify_password(form.password.data):
            if form.remember_me.data:
                login_user(user, remember=True)
            else:
                login_user(user)
            return redirect(url_for('home'))
        else:
            flash("Check your credentials and try again")
            return redirect(url_for('login'))

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():

        print(form.photo.data)
        users_like_yours = User.query.filter_by(email=form.email.data).first()
        print(users_like_yours)
        if users_like_yours is not None:
            flash("There is already an user with this email")
            return redirect(url_for('signup'))
        else:

            if form.photo.data is not None:
                pic = form.photo.data
                filename = secure_filename(pic.filename)
                mimetype = pic.mimetype
                print(mimetype)
                image = Images(picture=pic.read(), isUserProfile=True, isMissingPersonProfile=False, filename=filename,
                               mimetype=mimetype)
                hash_password = bcrypt.generate_password_hash(form.password.data.encode('utf8'))
                user = User(name=form.name.data, email=form.email.data,
                            password_hash=hash_password.decode('utf8'), profile_pic=image)

                db.session.add(user)
                db.session.add(image)
                db.session.commit()
                print("Usuário com imagem")
            else:
                hash_password = bcrypt.generate_password_hash(form.password.data.encode('utf8'))
                user = User(name=form.name.data, email=form.email.data,
                            password_hash=hash_password.decode('utf8'))
                db.session.add(user)
                db.session.commit()
                print("Usuário sem imagem")

            return redirect(url_for('login'))

    return render_template('signup.html', form=form)


@app.route('/signup-app', methods=['POST'])
def signup_app():
    users_like_yours = User.query.filter_by(request.get_json()["email"]).first()
    if users_like_yours is not None:
        return jsonify({
            "error": 1,
            "message": "Email is already in use"
        })
    else:
        email = request.get_json()["email"]
        hash_password = bcrypt.generate_password_hash(request.get_json()["password"].encode('utf8'))
        name = request.get_json()["name"]
        user = User(name=name, email=email,
                    password_hash=hash_password.decode('utf8'))
        db.session.add(user)
        db.session.commit()


@app.route('/login-app', methods=['POST'])
def login_app():
    user = User.query.filter_by().first(request.get_json()["email"])
    if user and user.verify_password(request.get_json()["password"]):
        login_user(user)
        return jsonify({"login": "successful"})
    else:
        return jsonify({"error": 2, "message": "Check your credentials and try again"})


@app.route('/video_feed')
@login_required
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

