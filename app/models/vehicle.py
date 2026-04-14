from sqlalchemy import column, Integer, Float, DateTime, Column
from datetime import datetime
from app.database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

    total_distance = Column(Float,default=0.0)

