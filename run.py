# run.py

from app.main import app
from app.database import create_database

def main():
    # 创建数据库表
    create_database()
    print("Database tables created.")

    # 启动 FastAPI 应用
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()