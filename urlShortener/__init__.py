from os.path import dirname, join

from restfulpy import Application as BaseApplication
from restfulpy.orm import DBSession


from urlShortener.controllers import Root
from urlShortener import models
from urlShortener.models.urls import Url

__version__ = '1.16.2'


class Application(BaseApplication):
    def __init__(self):
        super().__init__(
            'urlShortener',
            root=Root(),
            root_path=join(dirname(__file__), '..'),
            version=__version__,
        )

    # noinspection PyArgumentList
    def insert_basedata(self):  # pragma: no cover
        # basedata.insert()
        DBSession.commit()

    # noinspection PyArgumentList
    def insert_mockup(self):
        url = Url(url='www.google.com')
        DBSession.add(url)
        DBSession.commit


urlShortener = Application()
