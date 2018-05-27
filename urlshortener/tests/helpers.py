from restfulpy.testing import WebAppTestCase


import urlshortener


class WebTestCase(WebAppTestCase):
    application = urlshortener.urlshortener

