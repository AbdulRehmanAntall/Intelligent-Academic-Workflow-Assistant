from pydantic import BaseModel, Field

class TestModel(BaseModel):
    id: int = Field(..., description="Unique identifier for the test model")
    name: str = Field(..., description="Name of the test model")    
    description: str = Field(..., description="Description of the test model")
    