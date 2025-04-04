from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True, index=True)
    fname = Column(String, index=True)
    mname = Column(String, index=True)
    lname = Column(String, index=True)
    score = Column(Float)

class StudentCreate(BaseModel):
    fname: str
    mname: str
    lname: str
    student_id: int
    score: float
