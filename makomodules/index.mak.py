# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1526721920.9077945
_enable_loop = True
_template_filename = '/home/mohammad/workspace/projects/urlshortner/templates/index.mak'
_template_uri = 'index.mak'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<html>\n<head><title>Url shortener</title></head>\n<body>\n        <div style="background-color:DodgerBlue;color:white;padding:20px;">\n        <form method="POST" action="/urlshortener">\n        <strong>Iuput url:</strong>\n            <input type="text" name="url" />\n            <input type="submit" value="Submit" />\n        </form>\n        </div>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/mohammad/workspace/projects/urlshortner/templates/index.mak", "uri": "index.mak", "source_encoding": "ascii", "line_map": {"16": 0, "21": 1, "27": 21}}
__M_END_METADATA
"""
