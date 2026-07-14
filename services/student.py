from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.student import Student

def get_student_details_by_id(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    enrolled_courses = [enrollment.course for enrollment in student.enrollments]
    
    return {
        "id": student.id,
        "full_name": student.full_name,
        "status": student.status,
        "department": student.department,
        "courses": enrolled_courses
    }