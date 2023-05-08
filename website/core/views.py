from flask import render_template, Blueprint, flash, send_file, send_from_directory
from .forms import QuestionForm
from ..ai_service.ai_answers import string_answer

core = Blueprint("core", __name__)

questions: dict = {}  # ordered dict eliminates repeated calls with the same question
qa_list: list = []    # ordered list allows for printing questions in reverse order and repeated questions
start: bool = True
intro_message: bool = True


@core.route("/", methods=["GET", "POST"])
def index():
    form = QuestionForm()
    if questions:
        question = qa_list[-1][0]  # Use most recent question
    else:
        question = "Question"  # Use initial prompt

    if form.validate_on_submit():
        question = form.question.data
        form.question.data = None  # clear form so that placeholder question is shown
        # check for repeated question
        if question not in questions:
            answer = string_answer(question)
            questions[question] = answer
        answer = questions[question]
        flash(answer)
        qa_list.append((question, answer))
    return render_template("index.html", form=form, qa=qa_list, question=question)


@core.route("/about")
def about():
    return render_template("about.html")


@core.route('/download')
def download_resume():
    path = "static/"
    return send_from_directory(path, "sprunger_resume.pdf")
