# mysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel


# 配置 MySQL 数据库连接
DATABASE_URL = "mysql://root:2451671885@localhost/offDashboard"
engine = create_engine(DATABASE_URL)

# 创建数据库引擎和会话
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# 创建数据库表
Base.metadata.create_all(bind=engine)


# 获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 创建数据库表
def create_database():
    Base.metadata.create_all(bind=engine)