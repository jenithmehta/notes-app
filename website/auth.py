"""Authentication file"""
# pylint: disable=broad-exception-caught
import traceback
from flask import (
    Blueprint,
    render_template,
    request,
    flash,
)
from website.validation_models import SignupValidation
from website.models import User, db

# from website import db

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET"])
def login():
    """login"""
    return render_template("login.html", user={"is_authenticated": True})


@auth.route("/logout", methods=["GET"])
def logout():
    """logout"""
    return render_template("login.html", user={"is_authenticated": True})


@auth.route("/sign-up", methods=["GET", "POST"])
def signup():
    """signup"""
    if request.method == "POST":
        form_data = request.form
        try:
            signup_data = SignupValidation(**form_data)
            print(signup_data.model_dump())
            new_user = User(
                email=signup_data.email,
                password=signup_data.password1,
                first_name=signup_data.firstName,
            )
            db.session.add(new_user)
            db.session.commit()
            flash("Success!", "info")
        except Exception as err:
            trace_msg = traceback.format_exc()
            print(f"Error: {err}, Traceback: {trace_msg}")
    return render_template("sign_up.html", user={"is_authenticated": True})


@auth.route("/", methods=["GET"])
def home():
    """home"""
    return render_template("home.html", user={"is_authenticated": True})
