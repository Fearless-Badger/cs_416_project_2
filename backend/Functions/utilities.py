from Functions.pydantic_model import Student_pyd
 
def validate_stud_full(student: Student_pyd) -> bool:
    return(
        3 <= len(student.fname) <= 32 and
        3 <= len(student.mname) <= 32 and
        3 <= len(student.lname) <= 32 and
        0 <= student.score <= 100     and
        1 <= student.student_id <= 10
        )

def validate_id_only(student: Student_pyd)-> bool:
    return 1 <= student.student_id <= 10