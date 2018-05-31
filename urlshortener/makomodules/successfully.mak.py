# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1527584278.3637245
_enable_loop = True
_template_filename = '/home/mohammad/workspace/urlshortener/urlshortener/templates/successfully.mak'
_template_uri = 'successfully.mak'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        hash_id = context.get('hash_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<html>\n<head><title>Url shortener</title></head>\n<body>\n        <div style="background-color:MediumSeaGreen;color:white;padding:20px;">\n        <h2 style="text-align:center;">Successfully</h2>\n        <p style="text-align:center; color:black"><strong>Shortener\n        <a href="http://localhost:8080/urls/')
        __M_writer(str(hash_id))
        __M_writer('">\n        http://localhost:8080/urls/')
        __M_writer(str(hash_id))
        __M_writer('</a>\n        </strong></p>\n        </div>\n        \n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/mohammad/workspace/urlshortener/urlshortener/templates/successfully.mak", "uri": "successfully.mak", "source_encoding": "ascii", "line_map": {"16": 0, "22": 1, "23": 7, "24": 7, "25": 8, "26": 8, "32": 26}}
__M_END_METADATA
"""
