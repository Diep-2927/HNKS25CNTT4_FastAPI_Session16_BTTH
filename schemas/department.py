from pydantic import BaseModel

class DepartmentBase(BaseModel):
    id: int
    name: str