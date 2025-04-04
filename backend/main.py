from fastapi import FastAPI, HTTPException, Depends
from contextlib import asynccontextmanager
import json
import os
from sqlalchemy import create_engine, func
import pymysql
from sqlalchemy.orm import sessionmaker

from Functions.models import Base, Student, StudentCreate

# Need to map data to ORM
DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()
 
## Startup ##
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    pass # app shutdown sequence

# Get a reference to the database
def get_db():
    db = session_local()
    try:
        yield db
    except Exception as e:
        print(f"Error in function call 'def (get_db)' : \n{e}")
    finally:
        db.close()
 
@app.get("/list_all")
def read_students(db=Depends(get_db)):
    students = db.query(Student).all()
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

# Endpoint to create a new student
@app.post("/students/")
def create_student(student: StudentCreate, db=Depends(get_db)):
    db_student = Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# Endpoint to update a student's score
@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentCreate, db=Depends(get_db)):
    db_student = db.query(Student).filter(Student.student_id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    for key, value in student.dict().items():
        setattr(db_student, key, value)
    db.commit()
    return db_student

# Endpoint to delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db=Depends(get_db)):
    db_student = db.query(Student).filter(Student.student_id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(db_student)
    db.commit()
    return {"detail": "Student deleted"}

# Endpoint to calculate average score
@app.get("/students/average/")
def average_score(db=Depends(get_db)):
    avg_score = db.query(func.avg(Student.score)).scalar()
    return {"average_score": avg_score}

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