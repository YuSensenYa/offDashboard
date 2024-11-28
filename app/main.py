# app/main.py
from fastapi import FastAPI
from app.routers import sensor_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from app.routers.sensor_router import router
from fastapi.middleware.cors import CORSMiddleware
from app.middleware.cors import get_cors_middleware

app = FastAPI()
# 包含传感器相关的路由
app.include_router(sensor_router.router)
# 配置 API 路由
app.include_router(router, prefix="/api")

# 挂载静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")

# 应用跨域配置
get_cors_middleware(app)

# 将根路径 `/` 重定向到静态文件中的 `index.html`
@app.get("/")
async def read_root():
    return RedirectResponse(url="/static/index.html")


