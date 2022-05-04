from flask import Flask
from flask_migrate import Migrate
from app.model import tables
from app.model.tables import db


app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)

from app.controller import default





