from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from Backend.database import Base

class Outline(Base):
    __tablename__ = "outlines"
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    uploaded_file = Column(String, nullable=True)
    extracted_text = Column(Text, nullable=True)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())

    course = relationship("Course", back_populates="outline")
