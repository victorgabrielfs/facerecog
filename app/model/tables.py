from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    missing_people = db.relationship('MissingPeople', backref='user')
    profile_pic = db.relationship('Images', uselist=False)


    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.name


class MissingPeople(db.Model):
    __tablename__ = "missing_people"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    birthday = db.Column(db.DateTime, nullable=False)
    birthplace = db.Column(db.String(50), nullable=False)
    place_of_disappearance = db.Column(db.String(100), nullable=True)
    disappearance_details = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    pics = db.relationship('Images', backref='missing_person')

    def __init__(self, name, birthday, birthplace, place_of_disappearance, disappearance_details, user_id):
        self.name = name
        self.birthday = birthday
        self.birthplace = birthplace
        self.place_of_disappearance = place_of_disappearance
        self.disappearance_details = disappearance_details
        self.user_id = user_id

    def __repr__(self):
        return '<MissingPerson %r>' % self.name



class Images(db.model):
    __tablename__ = "images"
    id = db.Column(db.Integer, primary_key=True)
    picture = db.Column(db.LargeBinary, unique=True, nullable=False)
    isUserProfile = db.Column(db.Boolean, nullable=False)
    isMissingPersonProfile = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    missing_person_id = db.Column(db.Integer, db.ForeignKey('missing.people.id'), nullable=True)

    def __init__(self, picture, isUserProfile, isMissingPersonProfile, user_id, missing_person_id):
        self.picture = picture
        self.isUserProfile = isUserProfile
        self.isMissingPersonProfile = isMissingPersonProfile
        self.user_id = user_id
        self.missing_person_id = missing_person_id

    def __repr__(self):
        return '<Image %r>' % self.id