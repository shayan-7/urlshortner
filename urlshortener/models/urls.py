from sqlalchemy import Integer, String
from restfulpy.orm import DeclarativeBase, Field


class Url(DeclarativeBase):
    __tablename__ = 'urls'

    id = Field(Integer, primary_key=True, autoincrement=True)
    url = Field(String(50))

    # def __repr__(self):
    #     return "<User(url='%s')>" % (
    #         self.url
    #     )
