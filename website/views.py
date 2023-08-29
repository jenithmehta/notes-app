"""Views of Notes app"""
from flask import Blueprint, render_template

views = Blueprint("views",__name__)

@views.route("/", methods=["GET"])
def index():
    """ Index Html """
    return render_template("index.html")