from pydantic import BaseModel
from typing import List
from schemas.department import DepartmentBase
from schemas.course import CourseBase

class StudentDetailResponse(BaseModel):
    id: int
    full_name: str
    status: str
    department: DepartmentBase
    courses: List[CourseBase] = []