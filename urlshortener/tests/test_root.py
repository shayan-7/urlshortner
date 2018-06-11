import unittest

from bddrest.authoring import then, response

from urlshortener.tests.helpers import BDDTestClass


class RootTestCase(BDDTestClass):

    def test_root(self):
        call = dict(
            title='GET',
            description='',
            url='/',
            verb='GET',
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
            }
        )
        with self.given(**call):
            then(response.status_code == 200)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
