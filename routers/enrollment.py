from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.enrollment import EnrollmentCreate
from services.enrollment import enroll_course_for_student

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

@router.post("", status_code=status.HTTP_201_CREATED)
def create_enrollment(enrollment_data: EnrollmentCreate, db: Session = Depends(get_db)):
    return enroll_course_for_student(db, enrollment_data)