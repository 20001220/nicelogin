from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from nicelogin.models import Base

# 创建异步引擎
engine = create_async_engine("sqlite+aiosqlite:///../../database.db", echo=True)

# 创建异步会话工厂
async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False
)


# 初始化数据库，创建表
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
