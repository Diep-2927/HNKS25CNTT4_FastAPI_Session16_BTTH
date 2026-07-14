from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.student import Student
from models.course import Course
from models.enrollment import Enrollment
from schemas.enrollment import EnrollmentCreate


def enroll_course_for_student(db: Session, enrollment_data: EnrollmentCreate):
    student = db.query(Student).filter(Student.id == enrollment_data.student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    if student.status != "ACTIVE":
        raise HTTPException(status_code=400, detail="Student is not ACTIVE")

    course = db.query(Course).filter(Course.id == enrollment_data.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    if course.status != "OPEN":
        raise HTTPException(status_code=400, detail="Course is not OPEN")

    existing_enrollment = db.query(Enrollment).filter(
        Enrollment.student_id == enrollment_data.student_id,
        Enrollment.course_id == enrollment_data.course_id
    ).first()
    
    if existing_enrollment:
        raise HTTPException(status_code=400, detail="Student is already enrolled in this course")

    new_enrollment = Enrollment(
        student_id=enrollment_data.student_id,
        course_id=enrollment_data.course_id
    )
    
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)
    
    return {"message": "Enrollment created successfully", "enrollment_id": new_enrollment.id}