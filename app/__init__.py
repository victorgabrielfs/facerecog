from flask import Flask
from flask_migrate import Migrate
from app.model import tables
from app.model.tables import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://dgsitkfgyzkuev:5bab5efdefe1923873c82735d8dcc559c38c4fde5d6b4d6" \
                                        "666cc0b920754079b@ec2-3-230-122-20.compute-1.amazonaws.com:5432/d16l4f8fojv0d3"
db.init_app(app)
migrate = Migrate(app, db)

from app.controller import default





