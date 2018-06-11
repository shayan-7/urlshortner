from os.path import dirname, join

from restfulpy.authentication import Authenticator

from restfulpy import Application as BaseApplication
from restfulpy.orm import DBSession

from urlshortener.models.urls import Url
from .controllers.root import Root
__version__ = '0.1.0-planning.0'


class Application(BaseApplication):
    builtin_configuration = """
    messaging:
      default_sender: NueMDv.
      template_dirs:
        - %(root_path)s/urlshortener/templates

    """

    def __init__(self, application_name='urlshortener', root=Root()):
        super().__init__(
            application_name,
            root=root,
            root_path=join(dirname(__file__), '..'),
            version=__version__
        )

    # noinspection PyArgumentList
    def insert_basedata(self):  # pragma: no cover
        raise NotImplementedError()

    # noinspection PyArgumentList
    def insert_mockup(self):
        url = Url(url='http://www.varzesh3.com')
        DBSession.add(url)
        DBSession.commit()


urlshortener = Application()
