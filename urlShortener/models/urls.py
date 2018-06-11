
from sqlalchemy import String, Sequence, Integer
from restfulpy.orm import DeclarativeBase, Field

class Url(DeclarativeBase):
    __tablename__ = 'urls'

    id = Field(Integer, primary_key=True, autoincrement=True)
    url = Field(String(50))

