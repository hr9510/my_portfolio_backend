from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def createApp():
    app = Flask(__name__)

    app.config.update({
        "SQLALCHEMY_DATABASE_URI" : os.getenv("DATABASE_URL"),
        "SQLALCHEMY_TRACK_MODIFICATOINS" : False
    })

    db.init_app(app)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
