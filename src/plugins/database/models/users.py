from . import Base
from sqlalchemy import Column
from sqlalchemy import (
    INTEGER,
    TEXT
)

class Users(Base):
    __tablename__ = 'users'
    
    id:int = Column(INTEGER, primary_key=True, index=True)
    login:str = Column(TEXT)
    password:str = Column(TEXT)