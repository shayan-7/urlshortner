from sqlalchemy import Unicode, Integer
from restfulpy.orm import DeclarativeBase, Field, FilteringMixin, OrderingMixin


class Speciality(OrderingMixin, FilteringMixin, DeclarativeBase):
    __tablename__ = 'speciality'

    id = Field(Integer, primary_key=True)
    title = Field(Unicode(100), unique=True, index=True)

    __mapper_args__ = dict(order_by=title)
