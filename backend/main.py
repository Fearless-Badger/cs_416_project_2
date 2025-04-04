from fastapi import FastAPI, HTTPException, Depends
from contextlib import asynccontextmanager
import json
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel


from Functions.alchemy_model import Base, Student_db
from Functions.utilities import validate_stud_full
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
    # except Exception as e:
    #     print(f"Error in function call 'def (get_db)' : \n{e}")
    #     db.close()
    finally:
        db.close()

def validate_student_existence(student: Student_pyd, db=Depends(get_db)) -> bool:
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
        return {'result' : 'False',
                'message': 'Invalid data format.'}
    
    student_exists = validate_student_existence(student, db)

    if student_exists:
        return {
            'result' : 'False',
            'message': 'That student ID is taken!'
        }
    
    # Unpack pydantic model into dict, convert dict to SQLAlchemy model                                (I'm tired grandpa)
    db_student = Student_db(**student.model_dump())


    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return {
        'result' : 'True',
        'message': f'{student.fname} has been added to the class!'
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



## DO NOT HIT THE ENDPOINTS BELOW, they are just syntax references ##

items = []
items.append("apple")

@app.get("/")
def root():
    return {"Hello" : "World"} # Json

@app.get("/create")
def create_item(item: str):
    items.append(item)
    return json.dumps(items)

@app.get("/retrieve/{item_id}")
def retrieve_item(item_id: int):
    if -1 < item_id < len(items):
        return json.dumps(items[item_id])
    raise HTTPException(status_code=404, detail = "Item not found")