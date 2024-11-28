from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime
# 前端view类
# 用于响应传感器数据
class SensorDataOut(BaseModel):
    sensor_id: int  # 传感器 ID
    name: str  # 传感器名称
    location: str  # 传感器位置
    switch_status: bool  # 开关状态，True 表示开启，False 表示关闭
    temperature: Optional[float] = None  # 温度
    humidity: Optional[float] = None  # 湿度
    people_count: Optional[int] = None  # 人员计数
    voltage: Optional[float] = None  # 电压
    timestamp: Optional[datetime] = None  # 时间戳
    usage_duration: Optional[int] = None  # 使用时长（单位：小时）
    remark: Optional[str] = None  # 备注信息
    additional_data: Optional[Dict[str, Any]] = None  # 可扩展的其他数据

    class Config:
        orm_mode = True  # 确保 SQLAlchemy 数据模型可以被转换为 Pydantic 模型

    def __init__(self, **kwargs):
        # 使用default_factory来为additional_data设置默认值
        if 'additional_data' not in kwargs:
            kwargs['additional_data'] = {}
        super().__init__(**kwargs)