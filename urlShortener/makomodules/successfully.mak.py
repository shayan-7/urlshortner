# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1527935606.151157
_enable_loop = True
_template_filename = '/home/shayan/Desktop/urlShortener/urlShortener/templates/successfully.mak'
_template_uri = 'successfully.mak'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        hash_id = context.get('hash_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<html>\n<head>\n<title>Url shortener</title>\n\n<style>\n\n</style>\n<!-- Latest compiled and minified CSS -->\n<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">\n\n<!-- jQuery library -->\n<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n\n<!-- Popper JS -->\n<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>\n\n<!-- Latest compiled JavaScript -->\n<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>\n\n</head>\n<body data-gr-c-s-loaded="true">\n        <div class="container" style="background-color:lightGreen;color:white;padding:20px;margin-top:10px; border-radius:10px">\n        <h2 style="text-align:center;">Successfully</h2>\n        <p style="text-align:center; color:black"><strong>Shortener url: http://localhost:8080/')
        __M_writer(str(hash_id))
        __M_writer('</strong></p>\n        </div>\n\n\n\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/shayan/Desktop/urlShortener/urlShortener/templates/successfully.mak", "uri": "successfully.mak", "source_encoding": "ascii", "line_map": {"16": 0, "22": 1, "23": 24, "24": 24, "30": 24}}
__M_END_METADATA
"""
