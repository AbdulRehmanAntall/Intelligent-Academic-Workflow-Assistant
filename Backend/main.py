from fastapi import FastAPI
from Backend.database import engine, Base
from fastapi import FastAPI, Depends
from Backend.Routers import testroutes

app=FastAPI()

app.include_router(testroutes.router)
Base.metadata.create_all(bind=engine)
