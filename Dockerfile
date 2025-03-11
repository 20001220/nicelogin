# 使用官方 Python 3.10 镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录的内容到容器中
COPY . .

# 安装 Poetry
RUN pip install --no-cache-dir poetry -i https://mirrors.aliyun.com/pypi/simple

# 使用 poetry 安装项目依赖
RUN poetry install

# 暴露 NiceGUI 默认端口（假设 NiceGUI 使用 5000 端口）
EXPOSE 5000

# 使用 Poetry 创建的虚拟环境中的 Python 来启动应用
CMD ["poetry", "run", "python", "src/nicelogin/main.py"]
