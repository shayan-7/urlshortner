import unittest

from bddrest.authoring import then, response
from restfulpy.principal import JwtPrincipal

from urlshortener.tests.helpers import BDDTestClass, document_directory


class RootTestCase(BDDTestClass):

    def test_root(self):

        principal = JwtPrincipal(dict(
            email='mohammadsheikhian70@gmail.com',
            name='mohammad',
            family='sheikhian',
            id=1,
            sessionId=1,
            roles=['admin']
        ))
        self.login_token = principal.dump().decode("utf-8")

        call = dict(
            title='GET',
            description='',
            url='/',
            verb='GET',
            autodoc=f'{document_directory}/root_get_with_authorization_.md'
        )
        with self.given(**call):
            then(response.status_code == 200)

        self.login_token = None
        call = dict(
            title='GET',
            description='',
            url='/',
            verb='GET',
            autodoc=f'{document_directory}/root_get_without_authorization_.md'
        )
        with self.given(**call):
            then(response.status_code == 200)

        call = dict(
            title='POST',
            description='',
            url='/',
            verb='POST',
            form={
                'url': 'www.varzesh3.com'
            },
            autodoc=f'{document_directory}/root_post.md'
        )
        with self.given(**call):
            then(response.status_code == 200)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
