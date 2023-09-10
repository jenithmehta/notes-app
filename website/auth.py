"""Authentication file"""
import pydantic
from flask import Blueprint, render_template, request, jsonify
from website.validation_models import Signup_validation

auth = Blueprint("auth",__name__)

@auth.route("/login", methods=["GET"])
def login():
    """ login """
    return render_template("login.html",user={"is_authenticated":True})

@auth.route("/logout", methods=["GET"])
def logout():
    """ logout """
    return render_template("logut.html",user={"is_authenticated":True})

@auth.route("/sign-up", methods=["GET","POST"])
def signup():
    """ signup """
    if request.method == "POST":
        form_data = request.form
        signup_data = Signup_validation(**form_data)
        return signup_data.model_dump()
    return render_template("sign_up.html",user={"is_authenticated":True})

@auth.route("/", methods=["GET"])
def home():
    """ home """
    return render_template("home.html",user={"is_authenticated":True})
