from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from Backend.database import engine, Base, get_db
from Backend.models.testmodel import TestModel
from fastapi import FastAPI, Depends
from Backend.Routers import testroutes

app=FastAPI()

app.include_router(testroutes.router)
Base.metadata.create_all(bind=engine)
