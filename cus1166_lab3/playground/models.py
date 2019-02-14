from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Course(db.Model):
    __tablename__="course"

    id = db.Column(db.Integer, primary_key=True)
    course_number = db.Column(db.String, nullable = False)
    course_title = db.Column(db.String, nullable = False)



class RegisteredStudent(db.Model):
    __tablename__="registeredStudent"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    grade = db.Column(db.Integer, nullable = False)

#    def add_course(,seat):
#        new_ = Passenger(name=name, seat=seat, flight_id=self.id )
#        db.session.add(new_passenger)
#        db.session.commit()
