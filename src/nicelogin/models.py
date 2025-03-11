from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# 基类
Base = declarative_base()


# 用户模型
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(100))
