from flask import render_template, Blueprint, flash, send_from_directory, session
from .forms import QuestionForm, EmailForm
from ..ai_service.ai_answers import string_answer
from .. import mail, Message
from random import randint as randi

core = Blueprint("core", __name__)

questions: dict[dict] = {}  # ordered dict eliminates repeated calls with the same question
qa_list: list = []    # ordered list allows for printing questions in reverse order and repeated questions
start: bool = True
intro_message: bool = True


@core.route("/", methods=["GET", "POST"])
def index():
    if "n_questions" not in session.keys():
        session["n_questions"] = 0
    n_questions = session["n_questions"]
    form = QuestionForm()
    email_form = EmailForm()
    if questions:
        question = qa_list[-1][0]  # Use most recent question
    else:
        question = "Question"  # Use initial prompt

    # process Q/A form
    if form.validate_on_submit():
        n_questions += 1
        session["n_questions"] = n_questions
        question = form.question.data
        form.question.data = None  # clear form so that placeholder question is shown
        # check for repeated question
        if question not in questions:
            answer = string_answer(question)
            questions[question] = answer
        answer = questions[question]
        flash(answer)
        qa_list.append((question, answer))

    # process Email form
    if email_form.validate_on_submit():
        msg = Message(email_form.subject.data, sender='sprunger.joel@gmail.com', recipients=[email_form.email.data])
        msg.body = email_form.body.data
        mail.send(msg)

    return render_template("index.html",
                           form=form,
                           qa=qa_list,
                           question=question,
                           n_questions=n_questions,
                           email_form=email_form)


@core.route("/about")
def about():
    return render_template("about.html")


@core.route('/download')
def download_resume():
    path = "static/"
    return send_from_directory(path, "sprunger_resume.pdf")
