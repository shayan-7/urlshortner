# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1529302078.870025
_enable_loop = True
_template_filename = '/home/mohammad/workspace/urlshortener/urlshortener/templates/index.mak'
_template_uri = 'index.mak'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        name = context.get('name', UNDEFINED)
        family = context.get('family', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<html>\n<head><title>Url shortener</title></head>\n<body>\n        <div style="background-color:DodgerBlue;color:white;padding:20px;">\n        <h1>Profile: ')
        __M_writer(str(name))
        __M_writer(' ')
        __M_writer(str(family))
        __M_writer('</h1>\n        <form method="POST" action="/">\n        <strong>Iuput url:</strong>\n            <input type="text" name="url" />\n            <input type="submit" value="Submit" />\n        </form>\n        <form method="POST" action="/auth">\n            <input type="submit" value="Login" />\n        </form>\n        </div>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/mohammad/workspace/urlshortener/urlshortener/templates/index.mak", "uri": "index.mak", "source_encoding": "ascii", "line_map": {"16": 0, "23": 1, "24": 5, "25": 5, "26": 5, "27": 5, "33": 27}}
__M_END_METADATA
"""
