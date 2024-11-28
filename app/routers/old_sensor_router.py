# 模拟数据

from pydantic import BaseModel
from app.services import sensor_service
from app.models.sensor import SensorData

# @router.get("/data", response_model=SensorData)
# def get_sensor_data():
#     # 使用模拟数据
#     temp_humidity = sensor_service.get_temperature_humidity()
#     people_count = sensor_service.get_people_count()
#     return {
#         "temperature": temp_humidity["temperature"],
#         "humidity": temp_humidity["humidity"],
#         "people_count": people_count
#     }