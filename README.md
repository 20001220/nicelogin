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

### 3.服务器部署

我通过docker把这个项目部署在了我的云服务器上，开放了5000端口用来进行访问

```
相关docker命令
docker build -t nicelogin .
把数据库挂载出来
docker run -d --name nicelogin -p 5000:5000 -v $(pwd)/../docker/sqlite_data/database.db:/app/database.db nicelogin
可以通过下面这个ip+端口访问云服务器上的项目
http://123.207.48.210:5000
```

### 两次提交

1.实现了初始功能

2.添加一个简单的 **API** 用来返回登录之后的当前用户信息，并显示在网页上；调整了Dockerfile文件
