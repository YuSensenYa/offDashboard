# app/models/sensor.py
from app.database import Base
from sqlalchemy import (
    Column, Integer, String, Float, Boolean, DateTime, Text, JSON
)
from datetime import datetime

class SensorData(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    sensor_id = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    switch_status = Column(Boolean, nullable=False)
    temperature = Column(Float, nullable=True)
    humidity = Column(Float, nullable=True)
    people_count = Column(Integer, nullable=True)
    voltage = Column(Float, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    usage_duration = Column(Integer, nullable=True)
    remark = Column(Text, nullable=True)
    additional_data = Column(JSON, nullable=True)

    def __repr__(self):
        return f"<SensorData(sensor_id={self.sensor_id}, name={self.name}, location={self.location})>"