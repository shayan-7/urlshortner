from os.path import join, dirname, abspath

from nanohttp import settings
from restfulpy.testing import WebAppTestCase
from bddrest.authoring import given

from urlshortener import Application

client_secret_file = join(abspath(join(dirname(__file__), '..')),
                          'basedata/client_secrets.json')


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


from restfulpy.application import Application


# noinspection PyAbstractClass
class MockupApplication(Application):
    builtin_configuration = '''
    db:
      test_url: postgresql://postgres:postgres@localhost/urlshortener_test
      administrative_url: postgresql://postgres:postgres@localhost/postgres      
    logging:
      loggers:
        default:
          level: critical
    '''

    def configure(self, files=None, context=None, **kwargs):
        _context = dict(
            process_name='restfulpy_unittests'
        )
        if context:
            _context.update(context)
        super().configure(files=files, context=_context, **kwargs)
