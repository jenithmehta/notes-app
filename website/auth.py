"""Authentication file"""
from flask import Blueprint, render_template

auth = Blueprint("auth",__name__)

@auth.route("/login", methods=["GET"])
def login():
    """ login """
    return render_template("login.html")

@auth.route("/logout", methods=["GET"])
def logout():
    """ logout """
    return render_template("logut.html")

@auth.route("/signup", methods=["GET"])
def signup():
    """ signup """
    return render_template("signup.html")

@auth.route("/", methods=["GET"])
def home():
    """ home """
    return render_template("home.html")
