# 如何运行项目

## 本地运行

### 1. 克隆项目

```bash
git clone https://github.com/20001220/nicelogin.git
cd nicelogin
```

### 2. 安装 Poetry

如果未安装 Poetry，可以使用以下命令安装：

```bash
pip install poetry -i https://mirrors.aliyun.com/pypi/simple
```

### 3. 安装依赖

```bash
poetry install
```

### 4. 运行项目

```bash
poetry run python src/nicelogin/main.py
```

项目将在 `http://localhost:5000` 运行。

---

## Docker 运行

### 1. 构建 Docker 镜像

```bash
docker build -t nicelogin .
```

### 2. 运行容器

```bash
docker run -p 5000:5000 nicelogin
```

项目同样将在 `http://localhost:5000` 运行。

### 开发思路

- 使用 `NiceGUI` 框架快速构建 Web UI，提供简洁的交互。
- 采用 `SQLite` 存储用户数据，并使用 `SQLAlchemy` 进行 ORM 操作。
- 通过 `Poetry` 进行依赖管理，保证环境一致性。
- 采用 `asyncio` 进行异步操作，提高性能。

