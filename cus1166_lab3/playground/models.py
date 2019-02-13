from flask_sqlalchemy import SQLALchemy
db = SQLALchemy()

class Course(db.Models):
    __tablename__="course"

    id = db.Column(db.Integer, primary_key=True)
    course_number = db.Column(db.String, nullable = False)
    course_title = db.Column(db.String, nullable = False)

    def add_course(self,name,seat):
        new_passenger = Passenger(name=name, seat=seat, flight_id=self.id )
        db.session.add(new_passenger)
        db.session.commit()

class RegisteredStudent(db.Models):
    __tablename__="registeredStudent"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    grade = db.Column(db.Integer, nullable = False)
