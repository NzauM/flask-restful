from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy_serializer import SerializerMixin

# No Flask app initialization here.
# Assuming db and migrate are initialized in app.py
db = SQLAlchemy()
migrate = Migrate()


class Student(db.Model, SerializerMixin):
    # name,

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    pass
