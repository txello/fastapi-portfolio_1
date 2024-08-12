from . import Base
from sqlalchemy import Column
from sqlalchemy import (
    INTEGER,
    TEXT,
    TIMESTAMP
)

import datetime

class Tokens(Base):
    __tablename__ = 'tokens'
    
    id:int = Column(INTEGER, primary_key=True)
    userID:int = Column(INTEGER, index=True)
    projectID:int = Column(INTEGER, index=True)
    token:str = Column(TEXT)
    timestamp:datetime.datetime = Column(TIMESTAMP, default=datetime.datetime.now(datetime.UTC))