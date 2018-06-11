import unittest

from bddrest.authoring import then, response

from urlShortener.tests.helpers import BDDTestClass


class RootTestCase(BDDTestClass):

    def test_root(self):
        call = dict(
            title='GET',
            description='',
            url='/',
            verb='GET'
        )
        with self.given(**call):
            then(response.status_code == 200)

        call = dict(
            title='POST',
            description='',
            url='/',
            verb='POST',
            form={
                'url': 'www.google.com'
            }
        )
        with self.given(**call):
            then(response.status_code == 200)

        call = dict(
            title='GET',
            description='',
            url='/jR',
            verb='GET'
        )
        with self.given(**call):
            then(response.status_code == 302)

        call = dict(
            title='GET',
            description='',
            url='/IP5',
            verb='GET'
        )
        with self.given(**call):
            then(response.status_code == 400)

        call = dict(
            title='GET',
            description='',
            url='/g56',
            verb='GET'
        )
        with self.given(**call):
            then(response.status_code == 404)


if __name__ == '__main__':
    unittest.main()
