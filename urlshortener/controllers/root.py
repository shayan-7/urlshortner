from nanohttp import json, RestController, context
from restfulpy.controllers import JsonPatchControllerMixin
from restfulpy.orm import DBSession
from hashids import Hashids

import urlshortener
from urlshortener.controllers.auth import Auth
from urlshortener.controllers.urls import Urls
from urlshortener.models.urls import Url
from .helpers import template


hashids = Hashids(salt="url shortener")


class ApiV1(JsonPatchControllerMixin, RestController):

    @json
    def version(self):
        return {
            'version': urlshortener.__version__
        }


class Root(RestController):
    auth = Auth()
    urls = Urls()

    @template('index.mak')
    def get(self):
        return dict()

    @template('successfully.mak')
    def post(self):
        url = context.form.get('url')
        if not url.startswith('http'):
            url = f'http://{url}'

        url_exist = DBSession.query(Url).filter_by(url=url).one_or_none()

        if url_exist is None:
            url_exist = Url(url=url)
            DBSession.add(url_exist)
            DBSession.commit()

        hash_id = hashids.encode(url_exist.id)

        return dict(hash_id=hash_id)


if __name__ == '__main__':
    from nanohttp import quickstart, configure
    configure()
    try:
        quickstart(Root())
    except KeyboardInterrupt:
        print('CTLR+C just pressed')
