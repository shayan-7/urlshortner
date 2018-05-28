from nanohttp import settings
from restfulpy.testing import WebAppTestCase
from bddrest.authoring import given

from urlshortener import Application


class BDDTestClass(WebAppTestCase):
    application = Application()
    login_token = None

    @classmethod
    def configure_app(cls):
        super().configure_app()
        settings.merge('''
            logging:
              loggers:
                default:
                  level: debug
        ''')

    @classmethod
    def mockup(cls):
        cls.application.insert_mockup()

    def given(self, *args, **kwargs):
        if self.login_token:
            headers = kwargs.setdefault('headers', [])
            headers.append(('AUTHORIZATION', self.login_token))
        return given(self.application, *args, **kwargs)
