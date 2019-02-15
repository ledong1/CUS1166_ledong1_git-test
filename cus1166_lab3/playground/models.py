from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Course(db.Model):
    __tablename__= "course"

    id = db.Column(db.Integer, primary_key=True)
    course_number = db.Column(db.String, nullable = False)
    course_title = db.Column(db.String, nullable = False)

    def add_student(name,grade):
        new_student = RegisteredStudent(name=name, grade=grade)
        db.session.add(new_student)
        db.session.commit()


class RegisteredStudent(db.Model):
    __tablename__="registeredStudent"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    grade = db.Column(db.Integer, nullable = False)

#
