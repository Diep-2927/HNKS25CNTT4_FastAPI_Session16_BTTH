from fastapi import FastAPI
from database import Base, engine
from models import department, student, course, enrollment
from routers import student, enrollment

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Management System")

app.include_router(student.router)
app.include_router(enrollment.router)