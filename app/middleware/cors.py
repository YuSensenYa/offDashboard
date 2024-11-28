from fastapi.middleware.cors import CORSMiddleware


def get_cors_middleware(app):
    origins = [
        "http://localhost",           # 本地开发环境
        "http://localhost:8000",      # 本地服务器
        "https://your-frontend-url.com",  # 允许的其他前端地址
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,  # 允许的源
        allow_credentials=True,
        allow_methods=["*"],    # 允许所有请求方法 (GET, POST, PUT, DELETE, ...)
        allow_headers=["*"],    # 允许所有请求头
    )

