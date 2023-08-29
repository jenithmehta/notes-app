"""Authentication file"""
from flask import Blueprint, render_template

auth = Blueprint("auth",__name__)

@auth.route("/auth", methods=["GET"])
def authentication():
    """ authentication Html """
    return render_template("authentication.html")