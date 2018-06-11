from os.path import join, abspath, dirname

import functools
from mako.lookup import TemplateLookup
from nanohttp import action

here = abspath(join(dirname(__file__), '..'))
lookup = TemplateLookup(directories=[join(here, 'templates')],
                        module_directory=join(here, 'makomodules'))


def render_template(func, template_name):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)
        if hasattr(result, 'to_dict'):
            result = result.to_dict()
        elif not isinstance(result, dict):
            raise ValueError('The result must be an instance of dict, not: %s' %
                             type(result))

        template_ = lookup.get_template(template_name)
        return template_.render(**result)

    return wrapper


template = functools.partial(action, content_type='text/html',
                             inner_decorator=render_template)

