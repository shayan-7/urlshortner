from nanohttp import json, RestController, HttpNotFound, context, HttpFound, text, HttpBadRequest
from restfulpy.controllers import JsonPatchControllerMixin
from restfulpy.orm import DBSession
from hashids import Hashids

import urlshortener
from urlshortener.models.urls import Url
from .helpers import template


hashids = Hashids(salt="url shortener")


class DB:

    def store(self, url):

        if not url.startswith('http'):
            url = f'http://{url}'

        url_exist = DBSession.query(Url).filter_by(url=url).one_or_none()

        if url_exist is None:
            url_exist = Url(url=url)
            DBSession.add(url_exist)
            DBSession.commit()

        hash_id = hashids.encode(url_exist.id)
        return hash_id

    def resolve(self, hash_id):

        try:
            db_id, = hashids.decode(hash_id)
        except ValueError:
            raise HttpBadRequest()

        url = DBSession.query(Url).filter_by(id=db_id).one_or_none()
        if url is None:
            raise HttpNotFound()

        return url.url


db = DB()


class ApiV1(JsonPatchControllerMixin, RestController):

    @json
    def version(self):
        return {
            'version': urlshortener.__version__
        }


class Root(RestController):

    def _find_handler(self, remaining_paths):
        if len(remaining_paths) > 0:
            return self.resolve, remaining_paths
        return super()._find_handler(remaining_paths)

    @template('index.mak')
    def get(self):
        return dict()

    @template('successfully.mak')
    def post(self):
        return dict(hash_id=db.store(context.form.get('url')))

    @text
    def resolve(self, hexstring):
        raise HttpFound(db.resolve(hexstring))


if __name__ == '__main__':
    from nanohttp import quickstart, configure
    configure()
    try:
        quickstart(Root())
    except KeyboardInterrupt:
        print('CTLR+C just pressed')
