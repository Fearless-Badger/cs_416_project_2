from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Student_db(Base):
    __tablename__ = "user_data"
    student_id = Column(Integer, primary_key=True, index=True)
    fname = Column(String(20))
    mname = Column(String(20))
    lname = Column(String(20))
    score = Column(Integer)
