# 使用官方 Python 3.10 镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制 pyproject.toml 和 poetry.lock 文件，首先安装依赖
COPY pyproject.toml poetry.lock /app/

# 安装 Poetry
RUN pip install --no-cache-dir poetry -i https://mirrors.aliyun.com/pypi/simple

# 复制项目代码
COPY . .

# 使用 poetry 安装项目依赖
RUN poetry install

# 暴露 NiceGUI 端口
EXPOSE 5000

# 使用 Poetry 创建的虚拟环境中的 Python 来启动应用
CMD ["poetry", "run", "python", "src/nicelogin/main.py"]
