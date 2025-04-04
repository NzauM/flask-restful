# create 10 students
from models import Student, db
from faker import Faker
from app import app

fake = Faker()

with app.app_context():
    students = [Student(name=fake.name()) for i in range(10)]
    db.session.add_all(students)
    db.session.commit()
    print("All students added")