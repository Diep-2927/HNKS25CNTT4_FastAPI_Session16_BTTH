from database import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    status = Column(String(60), nullable=False)

    enrollments = relationship("Enrollment", back_populates="course")