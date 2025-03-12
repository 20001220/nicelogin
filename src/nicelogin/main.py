import asyncio
import httpx
from nicegui import app, ui
from nicelogin.logic import create_user, login_user
from nicelogin.database import init_db
from nicelogin.api import router


async def register(username: ui.input, password: ui.input, container: ui.row):
    # 执行操作
    result = await create_user(username.value, password.value)

    # 立即更新 UI
    with container:
        update_ui(result)

    # 如果注册成功，清空输入框
    if "成功" in result:
        username.value = ""
        password.value = ""


async def login(username: ui.input, password: ui.input, container: ui.row):
    # 执行操作
    result = await login_user(username.value, password.value)

    # 立即更新 UI
    with container:
        update_ui(result)

    # 如果登录成功，清空输入框
    if "欢迎" in result:
        # 登录成功后，获取用户信息并显示
        await show_user_info(username.value, container)
        username.value = ""
        password.value = ""


async def show_user_info(username: str, container: ui.row):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'http://localhost:5000/api/user/{username}')

        # 查找或创建专用信息容器
        info_container = None
        for child in container:  # 遍历容器子元素
            if getattr(child, '_info_container', False):  # 识别专用容器
                info_container = child
                break

        if not info_container:  # 首次创建带标识的容器
            with container:
                info_container = ui.column().classes('w-full')
                info_container._info_container = True  # 添加标识属性

        info_container.clear()  # 只清空信息容器内容

        if response.status_code == 200:
            user_info = response.json()
            user_info_str = f"用户名: {user_info['username']}\n注册时间: {user_info['created_at']}"
            with info_container:
                with ui.element('div').classes('w-full p-2 bg-blue-100 mb-2'):
                    ui.label(user_info_str).classes('text-center')
        else:
            with info_container:
                with ui.element('div').classes('w-full p-2 bg-red-100 mb-2'):
                    ui.label("获取用户信息失败").classes('text-center')


def update_ui(result: str):
    # 显示通知
    ui.notify(result)


def create_ui():
    with ui.row().classes('w-full justify-center') as container:
        username = ui.input(label="用户名").classes('w-64')
        password = ui.input(label="密码").props('type=password').classes('w-64')

        # 注册按钮
        ui.button("注册", on_click=lambda: asyncio.create_task(
            register(username, password, container)))
        # 登录按钮
        ui.button("登录", on_click=lambda: asyncio.create_task(
            login(username, password, container)))
    # 初始化数据库
    asyncio.run(init_db())  # 异步调用初始化函数
    # 启动应用
    ui.run(port=5000)


# 将路由器包含到应用中
app.include_router(router)

if __name__ in {"__main__", "__mp_main__"}:
    create_ui()
