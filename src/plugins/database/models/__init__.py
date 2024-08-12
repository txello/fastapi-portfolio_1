from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from .tokens import Tokens
from .users import Users