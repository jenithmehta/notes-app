import re
from pydantic import BaseModel, model_validator

class Signup_validation(BaseModel):
    email: str
    firstName: str
    password1: str
    password2: str

    @model_validator(mode='after')
    def check_passwords(self):
        pass1 = self.password1
        pass2 = self.password2
        if pass1 is not None and pass2 is not None and pass1!=pass2:
            raise ValueError("Passwords do not match")
        if len(pass1) < 8:
            raise ValueError("Length of password should be more than 8 characters")
        if not re.search("[A-Z]",pass1):
            raise ValueError("Password should include capital letters")
        if not re.search("[a-z]",pass1):
            raise ValueError("Password should include small letters")
        if not re.search("[0-9]",pass1):
            raise ValueError("Password should include numbers")
        if not re.search("[_@$%&*]",pass1):
            raise ValueError("Password should include special characters [_,@,$,%,&,*]")
        return self
    