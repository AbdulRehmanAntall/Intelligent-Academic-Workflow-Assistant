from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from Backend.database import Base

class UserQuestion(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=True)
    
    question_text = Column(Text, nullable=False)
    answer_text = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="questions")
    course = relationship("Course", back_populates="questions")
    task = relationship("Task", back_populates="questions")
    questions = relationship("UserQuestion", back_populates="course")

