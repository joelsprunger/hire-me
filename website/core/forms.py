from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email


class QuestionForm(FlaskForm):
    question = StringField("Question", validators=[DataRequired()])
    submit = SubmitField("Ask")


class EmailForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    subject = StringField("Subject", validators=[DataRequired()])
    body = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")
