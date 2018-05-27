import unittest


from urlshortener.tests.helpers import WebTestCase


class RootTestCase(WebTestCase):
    url = '/'

    def test_get_root(self):
        # Get template
        self.request('user', 'GET', self.url)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()

