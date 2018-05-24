from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///db.sqlite', echo=True)
Base = declarative_base()


class Url(Base):
    __tablename__ = 'urls'

    id = Column(Integer, Sequence('url_id_seq'), primary_key=True)
    url = Column(String(50))

    def __repr__(self):
        return "<User(url='%s')>" % (
            self.url)
