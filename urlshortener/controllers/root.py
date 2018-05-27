import binascii
import hashlib

from nanohttp import json, RestController, HttpNotFound, context, HttpFound, text
from restfulpy.controllers import JsonPatchControllerMixin, RootController

import urlshortener
from .helpers import template
from .urls import UrlController

db = {}


class Codec:

    def store(self, url):
        from pudb import set_trace; set_trace()
        if not url.startswith('http'):
            url = f'http://{url}'

        key = hashlib.sha1(url.encode()).digest()
        if key not in db:
            db[key] = url

        return binascii.hexlify(key).decode()

    def resolve(self, hexstring):
        hexstring = hexstring.encode()
        key = binascii.unhexlify(hexstring)
        if key not in db:
            raise HttpNotFound()

        return db[key]


codec = Codec()


class ApiV1(JsonPatchControllerMixin, RestController):
    # urls = UrlController()

    @json
    def version(self):
        return {
            'version': urlshortener.__version__
        }


class Root(RestController):
    apiv1 = ApiV1()

    def _find_handler(self, remaining_paths):
        if len(remaining_paths) > 0:
            return self.resolve, remaining_paths
        return super()._find_handler(remaining_paths)

    @template('index.mak')
    def get(self):
        return dict()

    @template('successfully.mak')
    def post(self):
        return dict(hash_id=codec.store(context.form.get('url')))

    @text
    def resolve(self, hexstring):
        raise HttpFound(codec.resolve(hexstring))

