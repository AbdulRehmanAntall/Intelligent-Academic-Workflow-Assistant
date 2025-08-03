from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship
import enum
from Backend.database import Base

class ResourceType(enum.Enum):
    LINK = "link"
    DOCUMENT = "document"
    VIDEO = "video"
    SLIDE = "slide"

class Resource(Base):
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    type = Column(Enum(ResourceType), nullable=False)
    title = Column(String, nullable=False)
    url = Column(String, nullable=True)
    description = Column(Text, nullable=True)

    task = relationship("Task", back_populates="resources")
