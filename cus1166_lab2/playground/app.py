from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

class_roster={
('a',100,'Freshman'),
('b',80,'Freshman'),
('c',76,'Senior'),
('d',97,'Freshman'),
('e',99,'Sophomore'),
('f',88,'junior'),
('g',68,'Freshman'),
('h',92,'Sophomore'),
('i',77,'Freshman')
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome/<string:student_name>")
def welcome(student_name):
    return render_template("welcome.html", student_name=student_name)

@app.route("/roster/<int:grade_view>")
def roster(grade_view):
    return render_template("roster.html", class_roster=class_roster, grade_view=grade_view)

if __name__ == "__main__":
    app.run()
