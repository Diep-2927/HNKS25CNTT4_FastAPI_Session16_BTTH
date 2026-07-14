from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.student import StudentDetailResponse
from services.student import get_student_details_by_id

router = APIRouter(prefix="/students", tags=["Students"])

@router.get("/{student_id}", response_model=StudentDetailResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    return get_student_details_by_id(db, student_id)