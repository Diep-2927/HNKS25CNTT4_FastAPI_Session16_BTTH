from pydantic import BaseModel

class CourseBase(BaseModel):
    id: int
    name: str
    status: str