from sqlalchemy import Integer, String
from restfulpy.orm import DeclarativeBase, Field


class Member(DeclarativeBase):
    __tablename__ = 'members'

    id = Field(Integer, primary_key=True, autoincrement=True)
    given_name = Field(String(50))
    family_name = Field(String(50))
    email = Field(String(50))
    google_access_token = Field(String(500))
    google_refresh_token = Field(String(500))
