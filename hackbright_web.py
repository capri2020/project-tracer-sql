"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    return render_template("student_info.html",first=first,last=last,github=github)


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-add")
def student_add():
    """Add a student."""

    return render_template("new_student.html")


@app.route("/student-add-confirmation", methods=['POST'])
def student_add_confirmation():
    """Add a student."""

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    github = request.form.get('github')

    hackbright.make_new_student(first_name=fname, last_name=lname, github=github)

    return render_template("new_student_success.html",github=github)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
