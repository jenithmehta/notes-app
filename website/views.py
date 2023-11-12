"""Views of Notes app"""
from flask import Blueprint, render_template
from website.models import db

views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
def index():
    """Index Html"""
    return render_template("home.html", user={"is_authenticated": False})
