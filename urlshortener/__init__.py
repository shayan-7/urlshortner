from os.path import dirname, join

from restfulpy.authentication import Authenticator

from restfulpy import Application as BaseApplication
from restfulpy.orm import DBSession
from urlshortener.models.member import Member

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
        member = Member(
            given_name='mohammad',
            family_name='sheikhian',
            email='mohammadsheikhian70@gmail.com',
            google_access_token='fgbsdibfosdnfosd',
            google_refresh_token='fgbdyugbdsiubgdufig'
        )
        DBSession.add(url)
        DBSession.add(member)
        DBSession.commit()


urlshortener = Application()
