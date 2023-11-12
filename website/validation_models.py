# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring

import re
from pydantic import BaseModel, model_validator
from flask import flash


# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
class SignupValidation(BaseModel):
    email: str
    firstName: str
    password1: str
    password2: str

    @model_validator(mode="after")
    def check_passwords(self):
        pass1 = self.password1
        pass2 = self.password2
        if pass1 and pass2 and pass1 != pass2:
            flash("Passwords do not match", "error")
            raise ValueError("Passwords do not match")
        # if len(pass1) < 8:
        #     flash("Length of password should be more than 8 characters", "error")
        #     raise ValueError("Length of password should be more than 8 characters")
        # if not re.search("[A-Z]", pass1):
        #     flash("Password should include capital letters", "error")
        #     raise ValueError("Password should include capital letters")
        # if not re.search("[a-z]", pass1):
        #     flash("Password should include small letters", "error")
        #     raise ValueError("Password should include small letters")
        # if not re.search("[0-9]", pass1):
        #     flash("Password should include numbers", "error")
        #     raise ValueError("Password should include numbers")
        # if not re.search("[_@$%&*]", pass1):
        #     flash("Password should include special characters [_,@,$,%,&,*]", "error")
        #     raise ValueError("Password should include special characters [_,@,$,%,&,*]")
        return self
