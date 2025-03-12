# api.py
from fastapi import APIRouter
from nicelogin.logic import get_user_info
from fastapi.responses import JSONResponse

router = APIRouter(prefix='/api')


# 添加一个 API 端点，返回用户信息
@router.get("/user/{username}")
async def api_get_user_info(username: str):
    user_info = await get_user_info(username)
    if user_info:
        return JSONResponse(content=user_info)
    return JSONResponse(content={"error": "用户不存在"}, status_code=404)
