from restfulpy.testing import ModelRestCrudTestCase

import urlshortener


class WebTestCase(ModelRestCrudTestCase):
    application = urlshortener.urlshortener

