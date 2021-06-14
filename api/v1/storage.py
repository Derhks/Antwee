from api.v1.app import app
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, TESTING


if TESTING:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)
migrate = Migrate(app, db)
