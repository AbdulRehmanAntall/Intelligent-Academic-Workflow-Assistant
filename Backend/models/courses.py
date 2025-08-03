from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from Backend.database import Base

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    semester_id = Column(Integer, ForeignKey("semesters.id"))
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    semester = relationship("Semester", back_populates="courses")
    outline = relationship("Outline", back_populates="course", uselist=False)
    tasks = relationship("Task", back_populates="course")
    questions = relationship("UserQuestion", back_populates="course")
