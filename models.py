from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

# No Flask app initialization here.
# Assuming db and migrate are initialized in app.py
db = SQLAlchemy()
migrate = Migrate()


class Student(db.Model, SerializerMixin):
    # name,
    @validates('name')
    def name_is_short(self,key,student_name):
        if len(student_name) < 5:
            raise ValueError("Student Name has to be greater than 5")
        return student_name
    
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    pass
