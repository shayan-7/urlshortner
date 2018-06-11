import unittest
from contextlib import contextmanager

from bddrest.authoring import then, response
from restfulpy.testing.mockup import http_server
from restfulpy.tests.helpers import MockupApplication
from nanohttp import RestController, settings, text

from urlshortener.tests.helpers import BDDTestClass


class OAuthMockupServer(RestController):
    @text
    def get(self):
        return 'code'


@contextmanager
def oauth_mockup_server(root_controller):
    app = MockupApplication('mockup-oauth', root_controller)
    with http_server(app) as (server, url):
        settings.merge(f'''
            tokenizer:
              url: {url}
        ''')
        yield app


class AuthTestCase(BDDTestClass):

    def test_auth(self):
        with oauth_mockup_server(OAuthMockupServer):

            call = dict(
                title='POST',
                description='',
                url='/auth',
                verb='POST',
            )
            with self.given(**call):
                then(response.status_code == 302)

            call = dict(
                title='GET',
                description='',
                url='/auth',
                verb='GET',
                query={
                    'state': 'sdfsd',
                    'code': 'sdfs',
                    'scope': 'asd'
                }
            )
            with self.given(**call):
                then(response.status_code == 200)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
