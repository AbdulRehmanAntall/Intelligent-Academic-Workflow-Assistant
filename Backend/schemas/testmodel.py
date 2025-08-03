from pydantic import BaseModel, Field

class TestModel(BaseModel):
    name: str = Field(..., description="Name of the test model")    
    description: str = Field(..., description="Description of the test model")
    