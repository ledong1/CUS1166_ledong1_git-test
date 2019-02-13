import sys
from flask import Flask, render_template,request
from flask_sqlalchemy import SQLALchemy
from config import Config
from models import Course, RegisteredStudent


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route("/")
def index():
    courses = Course.query.all()
    return render_template("index.html", courses = courses)

@app.route("/add_course", methods = ["post"])
def add_course():
    course_number = request.form.get("course_number")
    course_title = request.form.get("course_title")
    return render_template("index.html", student_name=student_name)

@app.route("/register_student", methods = ["post"])
def register_student():
    return render_template("roster.html", class_roster=class_roster, grade_view=grade_view)

if __name__ == "__main__":
    app.run()
