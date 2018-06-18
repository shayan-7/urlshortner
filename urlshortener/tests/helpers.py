from os.path import join, dirname, abspath

from restfulpy.authentication import Authenticator

from nanohttp import settings
from restfulpy.testing import WebAppTestCase
from bddrest.authoring import given

from urlshortener import Application

client_secret_file = join(abspath(join(dirname(__file__), '..')),
                          'basedata/client_secrets.json')

document_directory = join(abspath(join(dirname(__file__), '..')), 'document')


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


class MockupApplication(Application):
    def insert_basedata(self):
        pass

    builtin_configuration = '''
    db:
      test_url: postgresql://postgres:postgres@localhost/restfulpy_test
      administrative_url: postgresql://postgres:postgres@localhost/postgres      
    logging:
      loggers:
        default:
          level: critical
    '''

    def __init__(self, application_name, root):
        super().__init__(
            application_name,
            root=root
        )
        self.__authenticator__ = Authorization()

    def configure(self, files=None, context=None, **kwargs):
        _context = dict(
            process_name='restfulpy_unittests'
        )
        if context:
            _context.update(context)
        super().configure(files=files, context=_context, **kwargs)


class Authorization(Authenticator):

    def validate_credentials(self, credentials):
        pass

    def create_refresh_principal(self, member_id=None):
        pass

    def create_principal(self, member_id=None, session_id=None, **kwargs):
        pass

    def authenticate_request(self):
        pass
