# import statement and use base model

from pydantic import BaseModel


class Student(BaseModel):
    student_name : str
    student_email: str
    student_phone: str
