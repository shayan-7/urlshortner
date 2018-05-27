

from nanohttp import RestController, HttpNotFound, context, HttpFound, text

from .helpers import template

db = {}


class Codec:

    def store(self, url):
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


class UrlController(RestController):

    @template('successfully.mak')
    def post(self):
        return dict(hash_id=codec.store(context.form.get('url')))

    @text
    def get(self, hexstring):
        raise HttpFound(codec.resolve(hexstring))

