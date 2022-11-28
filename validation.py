from pydantic import BaseModel, Field, validator
import re


class BasicDetailsValid(BaseModel):
    name: str 
    email: str 
    phone: str

    class Config:
        orm_mode = True

    @validator('name')
    def is_valid_name(cls, val):
        if not val or len(val) < 3:
            raise ValueError("Invalid Name")
        return val

    @validator('phone')
    def is_valid_phone(cls, val):
        validphone = r"^\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{4})$"
        if not re.match(validphone,val):
             raise ValueError("Invalid Number")
        return val

    @validator('email')
    def is_valid_email(cls, val):
        validemail = r"^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if not re.match(validemail,val):
             raise ValueError("Invalid Number")
        return val

