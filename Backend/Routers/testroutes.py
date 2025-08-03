from typing import Annotated, List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from Backend.database import get_db
from Backend.models.testmodel import TestModel as TestModelDB
from Backend.schemas.testmodel import TestModel as TestModelSchema

router = APIRouter(
    prefix='/test',
    tags=['test']
    )


db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/testmodel", response_model=List[TestModelSchema])
def get_testmodels(db: db_dependency):
    return db.query(TestModelDB).all()

@router.post("/testmodelentry", response_model=TestModelSchema)
def create_testmodel(test_model: TestModelSchema, db: db_dependency):
    db_test_model = TestModelDB(**test_model.dict())
    db.add(db_test_model)
    db.commit()
    db.refresh(db_test_model)
    return db_test_model
