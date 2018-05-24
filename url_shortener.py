import hashlib
import binascii
import functools
from os.path import join, abspath, dirname
from mako.lookup import TemplateLookup
from nanohttp import Controller, RestController, context, html, text, HttpFound, Static, \
    settings, action, HttpNotFound
from hashids import Hashids


list_url = []
hashids = Hashids(salt='this is my salt')


here = abspath(dirname(__file__))
lookup = TemplateLookup(directories=[join(here, 'templates')], module_directory=join(here, 'makomodules'))


def render_template(func, template_name):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)
        if hasattr(result, 'to_dict'):
            result = result.to_dict()
        elif not isinstance(result, dict):
            raise ValueError('The result must be an instance of dict, not: %s' % type(result))

        template_ = lookup.get_template(template_name)
        return template_.render(**result)

    return wrapper


template = functools.partial(action, content_type='text/html', inner_decorator=render_template)


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


class Root(RestController):

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


if __name__ == '__main__':
    from nanohttp import quickstart, configure
    configure()
    try:
        quickstart(Root())
    except KeyboardInterrupt:
        print('CTLR+C just pressed')

