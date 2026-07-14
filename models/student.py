from database import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(60), nullable=False)
    status = Column(String(60), nullable=False)

    department_id = Column(Integer, ForeignKey('departments.id'))
    department = relationship("Department", back_populates='student')
    enrollments = relationship("Enrollment", back_populates="student")