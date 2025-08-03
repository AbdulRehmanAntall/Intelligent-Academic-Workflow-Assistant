from Backend.database import Base
from sqlalchemy import Column, Integer, String,DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Semester(Base):
    __tablename__ = "semesters"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)

    user = relationship("usrs", back_populates="semesters")
    courses = relationship("courses", back_populates="semester")