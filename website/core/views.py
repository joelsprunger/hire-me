from flask import render_template, Blueprint, flash
from .forms import QuestionForm
#from ..ai_service.ai_answers import string_answer
core = Blueprint("core", __name__)
qa = []


def string_answer(question: str):
    return "This is a test answer"


@core.route("/", methods=["GET", "POST"])
def index():
    form = QuestionForm()
    if form.validate_on_submit():
        question = form.question.data
        answer = string_answer(question)
        qa.append((question, answer))
        flash(answer)
    return render_template("index.html", form=form, qa=qa)
