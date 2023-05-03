from flask import render_template, Blueprint
core = Blueprint("core", __name__)


@core.route("/")
def index():
    return render_template("index.html")