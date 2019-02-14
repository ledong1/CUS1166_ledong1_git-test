import sys
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, Course, RegisteredStudent


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route("/")
def index():
    courses = Course.query.all()
    return render_template("index.html", courses = courses)

@app.route("/add_course", methods = ["POST"])
def add_course():
    course_number = request.form.get("course_number")
    course_title = request.form.get("course_title")
    course=Course(course_number=course_number,course_title=course_title)
    db.session.add(course)
    db.session.commit()
    courses = Course.query.all()
    return render_template("index.html", courses = courses)
 #student_name=student_name

@app.route("/register_student/<int:course_id>", methods = ["POST","GET"])
def register_student():
    return render_template("roster.html", class_roster=class_roster, grade_view=grade_view)

if __name__ == "__main__":
    app.run()
