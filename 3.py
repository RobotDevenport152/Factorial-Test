from fastapi import FastAPI
import uvicorn

# 路由模块（确保这3个文件中定义了 APIRouter 实例）
from api.book import api_book
from api.cbs import api_cbs
from api.zz import api_zz

app = FastAPI(title="Book Management API")

# 类似 Django 的 include 路由功能
app.include_router(api_book, prefix="/book", tags=["Book Interface"])
app.include_router(api_cbs, prefix="/cbs", tags=["Publisher Interface"])
app.include_router(api_zz, prefix="/zz", tags=["Author Interface"])

# 根路径
@app.get("/")
async def root():
    return {"message": "Hello World"}

# REST 风格测试接口（路径和方法一致）
@app.get("/get")
async def get():
    return {"method": "GET"}

@app.post("/post")
async def post():
    return {"method": "POST"}

@app.delete("/delete")
async def delete():
    return {"method": "DELETE"}

@app.put("/put")
async def put():
    return {"method": "PUT"}

@app.patch("/patch")
async def patch():
    return {"method": "PATCH"}

# 本地运行入口
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
