from fastapi import FastAPI
from app.database import engine, Base
from app.models import vehicle
from app.routes.vehicle import router as vehicle_router


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Fleet Tracking API is Running"}

@app.get("/health")
def health_check():
    return {"status": "Ok"}

app.include_router(vehicle_router)
Base.metadata.create_all(bind=engine)
