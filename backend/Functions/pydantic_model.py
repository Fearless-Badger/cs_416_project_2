from pydantic import BaseModel

class Student_pyd(BaseModel):
    fname: str | None = None
    mname: str | None = None
    lname: str | None = None
    score: int | None = None
    student_id: int