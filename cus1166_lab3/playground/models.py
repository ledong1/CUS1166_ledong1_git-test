from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Course(db.Model):
    __tablename__= "course"

    id = db.Column(db.Integer, primary_key=True)
    course_number = db.Column(db.String, nullable = False)
    course_title = db.Column(db.String, nullable = False)

    registeredStudents = db.relationship("RegisteredStudent", backref="course", lazy=True)

    def add_student(self,name,grade):
        new_student = RegisteredStudent(name=name, grade=grade, course_id=self.id)
        db.session.add(new_student)
        db.session.commit()


class RegisteredStudent(db.Model):
    __tablename__="registeredStudent"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    grade = db.Column(db.Integer, nullable = False)

    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
#
