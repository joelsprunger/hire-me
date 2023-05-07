from flask import render_template, Blueprint, flash, send_file, send_from_directory
from .forms import QuestionForm
from ..ai_service.ai_answers import string_answer

core = Blueprint("core", __name__)
qa = []


@core.route("/", methods=["GET", "POST"])
def index():
    form = QuestionForm()
    if form.validate_on_submit():
        question = form.question.data
        answer = string_answer(question)
        qa.append((question, answer))
        flash(answer)
    return render_template("index.html", form=form, qa=qa)


@core.route("/about")
def about():
    return render_template("about.html")


@core.route('/download')
def download_resume():
    path = "static/"
    return send_from_directory(path, "sprunger_resume.pdf")
