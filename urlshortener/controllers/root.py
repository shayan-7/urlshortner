from nanohttp import json, RestController
from restfulpy.controllers import JsonPatchControllerMixin, RootController

import urlshortener
from .helpers import template
from .urls import UrlController


class ApiV1(JsonPatchControllerMixin, RestController):
    urls = UrlController()

    @json
    def version(self):
        return {
            'version': urlshortener.__version__
        }


class Root(RootController):
    apiv1 = ApiV1()

    @template('index.mak')
    def index(self):
        return dict()
