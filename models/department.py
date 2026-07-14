from sqlalchemy import Column, String, Integer
from database import Base
from sqlalchemy.orm import relationship

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    student = relationship("Student", back_populates="department")