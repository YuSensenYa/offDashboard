# # app/services/sensor_service.py

from sqlalchemy.orm import Session
from app.models.sensor import SensorData

# 确保获取到数据
def get_latest_sensor_data(db: Session):
    sensor_data = db.query(SensorData).order_by(SensorData.id.desc()).first()
    if sensor_data is None:
        return {"error": "No data found"}
    return sensor_data