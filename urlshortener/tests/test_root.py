import unittest

from urlshortener.tests import helpers


class RootTestCase(helpers.WebTestCase):
    url = '/'

    def test_get_root(self):

        # Get template
        result, ___ = self.request('user', 'GET', self.url)
        expected_result = b'<html>\n<head><title>Url shortener</title></head>\n<body>\n        <div style="background-color:DodgerBlue;color:white;padding:20px;">\n        <form method="POST" action="/urlshortener">\n        <strong>Iuput url:</strong>\n            <input type="text" name="url" />\n            <input type="submit" value="Submit" />\n        </form>\n        </div>\n</body>\n</html>\n'
        self.assertEquals(result, expected_result)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
