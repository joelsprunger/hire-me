from flask import render_template, Blueprint, flash, send_from_directory, session, url_for
from .forms import QuestionForm, EmailForm
from ..ai_service.ai_answers import string_answer
from .. import mail, Message

core = Blueprint("core", __name__)

questions: dict = {}  # ordered dict eliminates repeated calls with the same question
qa_list: list = []    # ordered list allows for printing questions in reverse order and repeated questions
start: bool = True
intro_message: bool = True


def session_init() -> None:
    # initialize new session variables
    resume_link = url_for("core.download_resume")
    about_link = url_for("core.about")
    github_link = "https://github.com/joelsprunger/personal-website"
    garden_link = "https://www.instagram.com/portlandgarden/"
    session["html_links"] = {
            "Joel's resume": f'<a href={resume_link} target="_blank">Joel''s resume</a>',
            "About this app": f'<a href={about_link}>About</a>',
            "GitHub": f'<a href={github_link} target="_blank">GitHub</a>',
            "Gardening": f'<a href={garden_link} target="_blank">Gardening</a>',
            "gardening": f'<a href={garden_link} target="_blank">gardening</a>',
            "Garden": f'<a href={garden_link} target="_blank">Garden</a>',
            "garden": f'<a href={garden_link} target="_blank">garden</a>'}

    if "questions" not in session.keys():
        session["questions"]: dict = {}
    if "qa_list" not in session.keys():
        session["qa_list"]: list = []


@core.route("/", methods=["GET", "POST"])
def index():
    # session.clear()
    if "html_links" not in session.keys():
        session_init()
    form = QuestionForm()
    email_form = EmailForm()
    if session["questions"]:
        question = session["qa_list"][-1][0]  # Use most recent question
    else:
        question = "Question"  # Use initial prompt

    # process Q/A form
    if form.validate_on_submit():
        question = form.question.data
        form.question.data = None  # clear form so that placeholder question is shown
        # check for repeated question
        if question not in session["questions"]:
            answer = string_answer(question)
            for word, link in session["html_links"].items():
                if word+"ing" in answer:
                    continue  # don't replace gardening with <garden>ing
                else:
                    answer = answer.replace(word, link)

            session["questions"][question] = answer
        answer = session["questions"][question]
        flash(answer)
        session["qa_list"].append((question, answer))

    # process Email form
    if email_form.validate_on_submit():
        msg = Message(email_form.subject.data, sender='sprunger.joel@gmail.com', recipients=[email_form.email.data])
        msg.body = email_form.body.data
        mail.send(msg)

    return render_template("index.html",
                           form=form,
                           qa=session["qa_list"],
                           question=question,
                           n_questions=len(session["qa_list"]),
                           email_form=email_form)


@core.route("/about")
def about():
    return render_template("about.html")


@core.route('/download')
def download_resume():
    path = "static/"
    return send_from_directory(path, "sprunger_resume.pdf")
