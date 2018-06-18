import unittest

from bddrest.authoring import then, response

from urlshortener.tests.helpers import BDDTestClass, document_directory


class UrlsTestCase(BDDTestClass):

    def test_urls(self):

        call = dict(
            title='GET',
            description='',
            url='/urls/zK',
            verb='GET',
            autodoc=f'{document_directory}/urls_get_.md'
        )
        with self.given(**call):
            then(response.status_code == 302)

        call = dict(
            title='GET',
            description='',
            url='/urls/lP5',
            verb='GET'
        )
        with self.given(**call):
            then(response.status_code == 400)

        call = dict(
            title='GET',
            description='',
            url='/urls/lP',
            verb='GET'
        )
        with self.given(**call):
            then(response.status_code == 404)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
