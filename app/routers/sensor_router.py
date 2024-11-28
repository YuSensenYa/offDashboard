# # app/routers/sensor_router.py

from http.client import HTTPException
from fastapi import APIRouter,Depends
router = APIRouter()

from sqlalchemy.orm import Session
from app.services.sensor_service import get_latest_sensor_data
from app.database import get_db
from app.models.schemas import SensorDataOut


# 路由：获取传感器数据
@router.get("/data", response_model=SensorDataOut)
def get_sensor_data(db: Session = Depends(get_db)):
    sensor_data = get_latest_sensor_data(db)
    if sensor_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return sensor_data