# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1526721980.4338439
_enable_loop = True
_template_filename = '/home/mohammad/workspace/projects/urlshortner/templates/notfoundpage.html'
_template_uri = 'notfoundpage.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<html>\n<head><title>Url shortener</title></head>\n<body style="padding:80px;">\n            <div style="background-color:Gray;color:white;padding:20px;">\n            <h1 style="text-align:center;">Can not found page</h1>\n            </div>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/mohammad/workspace/projects/urlshortner/templates/notfoundpage.html", "uri": "notfoundpage.html", "source_encoding": "ascii", "line_map": {"16": 0, "21": 1, "27": 21}}
__M_END_METADATA
"""
