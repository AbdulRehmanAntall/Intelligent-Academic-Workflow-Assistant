from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Backend.database import Base

class TestModel(Base):
    __tablename__ = 'testmodel'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    
    # Example of a relationship if needed
    # related_model_id = Column(Integer, ForeignKey('relatedmodel.id'))
    # related_model = relationship("RelatedModel", back_populates="testmodels")