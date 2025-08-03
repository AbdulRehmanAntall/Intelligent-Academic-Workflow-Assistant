from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Backend.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)  
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    bio = Column(String, default="")
    profile_picture = Column(String, default="default.jpg")

    semester=relationship("Semester", back_populates="user")
    ai_requests=relationship("AIRequest", back_populates="user")
    questions = relationship("UserQuestion", back_populates="user")

