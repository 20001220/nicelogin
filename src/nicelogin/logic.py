# logic.py
import hashlib
from nicelogin.database import async_session
from nicelogin.models import User
from sqlalchemy.future import select

PEPPER = "fixed_pepper_value"  # 正常应存储在安全配置中


def hash_password(password: str) -> str:
    """加盐哈希处理"""
    salted = password + PEPPER
    return hashlib.sha256(salted.encode()).hexdigest()


# 用户注册功能
async def create_user(username: str, password: str):
    async with async_session() as session:
        async with session.begin():
            if username == "" or password == "":
                return "用户名和密码注册时不能为空"
            # 检查用户名是否已存在
            result = await session.execute(select(User).filter_by(username=username))
            existing_user = result.scalars().first()
            if existing_user:
                return "用户名已存在"

            # 创建新用户
            new_user = User(username=username, password=hash_password(password))
            session.add(new_user)
            await session.commit()
            return "注册成功"


# 用户登录功能
async def login_user(username: str, password: str):
    async with async_session() as session:
        if username == "" or password == "":
            return "请输入用户名或密码"
        stmt = select(User).filter_by(username=username)
        result = await session.execute(stmt)
        user = result.scalars().first()

        if user and user.password == hash_password(password):
            return f"欢迎，{username}"
        return "用户名或密码错误"


# 用户查询功能
async def get_user_info(username: str) -> dict:
    async with async_session() as session:
        result = await session.execute(
            select(User).filter_by(username=username)
        )
        user = result.scalars().first()
        return {
            "username": user.username,
            "created_at": user.created_at.isoformat()
        } if user else None
