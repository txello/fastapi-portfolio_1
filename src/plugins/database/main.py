from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

engine = create_async_engine("mysql+aiomysql://root:@127.0.0.1/Tasks")
Session = async_sessionmaker(engine)