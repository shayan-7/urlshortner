from os.path import dirname, join

from restfulpy import Application as BaseApplication
from .controllers.root import Root

__version__ = '0.1.0-planning.0'


class Application(BaseApplication):
    builtin_configuration = """
    messaging:
      default_sender: NueMDv.
      template_dirs:
        - %(root_path)s/urlshortener/templates

    """

    def __init__(self):
        super().__init__(
            'urlshortener',
            root=Root(),
            root_path=join(dirname(__file__), '..'),
            version=__version__,
        )

    # noinspection PyArgumentList
    def insert_basedata(self):  # pragma: no cover
        raise NotImplementedError()

    # noinspection PyArgumentList
    def insert_mockup(self):
        raise NotImplementedError()


urlshortener = Application()

