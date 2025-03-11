import asyncio
from nicegui import ui
from nicelogin.logic import create_user, login_user
from nicelogin.database import init_db


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
        username.value = ""
        password.value = ""


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


if __name__ in {"__main__", "__mp_main__"}:
    create_ui()
