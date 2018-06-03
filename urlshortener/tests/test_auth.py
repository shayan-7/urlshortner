from bddrest.authoring import then, response

from urlshortener.tests.helpers import BDDTestClass


class AuthTestCase(BDDTestClass):

    def test_auth(self):

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
