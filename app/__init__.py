from flask import Flask
from .database import db
from .routes import app as sample_app

def create_app():
    app = Flask(__name__)

    # TODO DBはsqliteなので、dockerでpostgresに変更
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employee.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(sample_app)

    with app.app_context():
        db.create_all()

    return app
