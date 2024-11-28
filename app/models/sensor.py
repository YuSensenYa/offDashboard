# app/models/sensor.py
from sqlalchemy import Column, Integer, Float
from app.database import Base

class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)  # 主键ID
    temperature = Column(Float)  # 温度字段
    humidity = Column(Float)  # 湿度字段
    people_count = Column(Integer)  # 人数字段