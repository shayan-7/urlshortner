import functools
from os.path import join, abspath, dirname
from mako.lookup import TemplateLookup
from nanohttp import Controller, RestController, context, html, text, HttpFound, Static, settings, action
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


class UrlShortenerController(RestController):
    @template('successfully.mak')
    def post(self):
        url = context.form.get('url')
        from pudb import set_trace; set_trace()

        if url in list_url:
            key = list_url.index(url)
        else:
            key = len(list_url)
            list_url.append(url)

        hash_id = hashids.encode(key)
        return dict(
            hash_id=hash_id
        )


class UrlIdController(RestController):
    @template('notfoundpage.html')
    def get(self, url_id: str=None):
        print('url id: ', url_id)

        try:
            if url_id != None:
                key = hashids.decode(url_id)[0]
                print('key ', key)

                if key < len(list_url):
                    url = list_url[key]
                else:
                    url = None
            else:
                url = None
        except:
            url = None

        print('url: ', url)

        if url != None:
            if 'http://' in url:
                raise HttpFound(url)
            else:
                raise HttpFound('http://' + url)
        else:
            return dict()


class Root(Controller):
    urlshortener = UrlShortenerController()
    urlid = UrlIdController()

    @template('index.mak')
    def index(self):
        return dict( )

