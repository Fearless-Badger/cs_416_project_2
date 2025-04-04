from fastapi import FastAPI, HTTPException, Depends
from contextlib import asynccontextmanager
import json
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel


from Functions.alchemy_model import Base, Student_db
from Functions.utilities import validate_stud_full, validate_id_only
from Functions.pydantic_model import Student_pyd


# ORM
DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()
 
## Startup ##
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    pass # app shutdown sequence



# Utility functions

# Get a reference to the database
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

def validate_student_existence(student: Student_pyd, db: Session) -> bool:
    student_exists = db.query(Student_db).filter(Student_db.student_id == student.student_id).first()
    #               query db  =>       where student_id === given pydantic model student_id
    #
    # "Student_db" => Database model in Functions/alchemy_model.py
    # "student"    => Pydantic model in Functions/pydantic_model.py
    return student_exists is not None


##############################################

@app.post("/add_student")
def upload_student(student: Student_pyd, db=Depends(get_db)):

    valid_format = validate_stud_full(student)

    if not valid_format:
        return {'result' : 'false',
                'message': 'Invalid data format.'}
    
    student_exists = validate_student_existence(student, db)

    if student_exists:
        return {
            'result' : 'false',
            'message': 'That student ID is taken!'
        }
    
    # Unpack pydantic model into dict, convert dict to SQLAlchemy model                                (I'm tired grandpa)
    db_student = Student_db(**student.model_dump())


    db.add(db_student)
    db.commit()

    return {
        'result' : 'true',
        'message': f'{student.fname} has been added to the class!'
    }

@app.post("/delete_student")
def delete_student(student: Student_pyd, db=Depends(get_db)):

    if not validate_id_only(student):
        return {
            'result' : 'false',
            'message': 'Invalid data format.'
        }
    
    if not validate_student_existence(student, db):
        return {
            'result' : 'false',
            'message': 'This student does not exist.'
        }
    
    try:    
        db_student = db.query(Student_db).filter(Student_db.student_id == student.student_id).first()
        db_student_name = db_student.fname
        if db_student:
            db.delete(db_student)
            db.commit()
        
        return {
            'result' : 'true',
            'message': f'{db_student_name} has been removed from the class.'
        }
    
    except Exception as e:
        print(f"Error in /delete_student route: {e}")
        return {
        'result' : 'false',
        'message': 'Error when interacting with database.' 
        }
        
    
 
@app.get("/list_all")
def read_students(db=Depends(get_db)):
    students = db.query(Student_db).all()
    student_list = []
    for student in students:
        student_list.append({
            "fname" : student.fname,
            "mname" : student.mname,
            "lname" : student.lname,
            "student_id" : student.student_id,
            "score" : student.score
        })
    return student_list
