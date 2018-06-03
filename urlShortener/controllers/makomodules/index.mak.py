# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1527586793.4194257
_enable_loop = True
_template_filename = '/home/shayan/Desktop/urlShortener/urlShortener/templates/index.mak'
_template_uri = 'index.mak'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<html class="gr__localhost"><head>\n<title>Url shortener</title>\n<style>\n\n</style>\n<!-- Latest compiled and minified CSS -->\n<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">\n\n<!-- jQuery library -->\n<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n\n<!-- Popper JS -->\n<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>\n\n<!-- Latest compiled JavaScript -->\n<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>\n\n</head>\n<body data-gr-c-s-loaded="true">\n\n\n      <div class="container" style="background-color: orange;color: #28a745;padding:20px;border-radius:10px;margin-top:10px;">\n      <div class="col-md-6 col-md-offset-8">\n\t\t\t<form style="align:center" method="POST" action="/" class="form-inline col-md-12">\n        \t<p style="display:inline; margin:10px; font-size:25px">Iuput url:</p>\n            <input style="display:inline; padding:5px;" type="text" name="url">\n            <input style="display:inline; margin:10px" type="submit" value="Submit" class="btn btn-success">\n        \t</form>\n\t\t</div>\n\t    </div>\n\n\n\n\n\n\n</body></html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/shayan/Desktop/urlShortener/urlShortener/templates/index.mak", "uri": "index.mak", "source_encoding": "ascii", "line_map": {"16": 0, "21": 1, "27": 21}}
__M_END_METADATA
"""
