from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.vehicle import Vehicle
from app.services.utils import calculate_distance
from app.services.redis_client import redis_client
import json

router = APIRouter()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/vehicle/update")
def update_vehicle(id: int, latitude: float, longitude: float, db: Session = Depends(get_db)):
    # vehicle = Vehicle(id=id, latitude=latitude, longitude=longitude)
    # if(db.query(Vehicle).filter(Vehicle.id == id).first()):
    #     db.query(Vehicle).filter(Vehicle.id == id).update(
    #         {Vehicle.latitude : latitude,
    #          Vehicle.longitude : longitude})
    #     db.commit()
    # else:
    #     db.add(vehicle)
    #     db.commit()
    vehicle = db.query(Vehicle).filter(Vehicle.id == id).first()

    if vehicle:
        dist = calculate_distance(vehicle.latitude, vehicle.longitude,
                                  latitude, longitude)
        vehicle.total_distance += dist
        vehicle.latitude = latitude
        vehicle.longitude = longitude
        if dist < 0.0001:
            print(f"Vehicle {id} might be stopped")
    else:
        vehicle = Vehicle(id=id, latitude=latitude, longitude=longitude, total_distance=0.0)
        db.add(vehicle)

    db.commit()

    redis_client.set(f"vehicle:{id}",
                     json.dumps({"latitude": latitude,
                                 "longitude": longitude}))

    return {"message": "Vehicle updated",
            "total_distance": vehicle.total_distance}

@router.get("/vehicle/{id}")
def get_vehicle(id: int, db: Session = Depends(get_db)):

    cached = redis_client.get(f"vehicle:{id}")
    if cached:
        return json.loads(cached)

    vehicle = db.query(Vehicle).filter(Vehicle.id == id).first()
    return vehicle


