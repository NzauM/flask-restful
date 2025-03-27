from flask import Flask, request, jsonify

from models import Student, db, migrate # Import db and migrate from models.py

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app) # Initialize db with the app
migrate.init_app(app, db) # Initialize migrate with app and db

@app.route('/students', methods=['GET'])
def get_all_students():
    """Returns a list of all students."""
    all_students = Student.query.all()
    students_list = [std.to_dict() for std in all_students]
    return jsonify(students_list)

@app.route('/students', methods=['POST'])
def create_student():
    """Creates a new student."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid data"}), 400
    try:
        new_student = Student(name=data['name'])
        db.session.add(new_student)
        db.session.commit()
        return jsonify(new_student.to_dict()), 201
    except KeyError:
        return jsonify({"error": "Missing required fields"}), 400

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    """Returns a single student by ID."""
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student.to_dict())

@app.route('/students/<int:student_id>', methods=['PATCH'])
def update_student(student_id):
    """Updates a student's information by ID."""
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid data"}), 400
    try:
        if 'name' in data:
            student.name = data['name']
        db.session.commit()
        return jsonify(student.to_dict())
    except KeyError:
        return jsonify({"error": "Invalid fields"}), 400

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    """Deletes a student by ID."""
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
