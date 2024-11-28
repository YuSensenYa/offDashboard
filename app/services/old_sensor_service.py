# # app/services/sensor_service.py
# import random
# from app.models.sensor import SensorData



# 先使用模拟数据
# app/services/sensor_service.py
import random
import time
from app.models.sensor import SensorData

# # 模拟温湿度数据
# def get_temperature_humidity():
#     # 模拟温度范围在 20 到 30°C 之间，湿度范围在 30 到 70% 之间
#     temperature = round(random.uniform(20.0, 30.0), 2)
#     humidity = round(random.uniform(30.0, 70.0), 2)
#     return {"temperature": temperature, "humidity": humidity}
#
# # 模拟人数数据
# def get_people_count():
#     # 模拟办公室人数范围在 0 到 20 人之间
#     people_count = random.randint(0, 20)
#     return people_count
#

from sqlalchemy.orm import Session
from app.models.sensor import SensorData

