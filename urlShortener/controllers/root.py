from nanohttp import HttpFound, HttpNotFound, HttpBadRequest, context, \
    json, RestController, text
from restfulpy.controllers import JsonPatchControllerMixin
from restfulpy.orm import DBSession
from hashids import Hashids

import urlShortener
from urlShortener.models.urls import Url
from urlShortener.controllers.helper import template

# for using hashids we must make a instance from Hashids()
hashids = Hashids('')


# DB class stores and restores urls in 'Url' Database
class DB:

    def store(self, url):

        if not url.startswith('http'):
            url = f'http://{url}'

        url_exist = DBSession.query(Url).filter_by(url=url).one_or_none()

        if url_exist is None:
            new_url = Url(url=url)
            DBSession.add(new_url)
            DBSession.commit()

        else:
            new_url = url_exist
        hash_id = hashids.encode(new_url.id)
        return hash_id

    def resolve(self, hash_id):

        try:
            db_id, = hashids.decode(hash_id)
        except ValueError:
            raise HttpBadRequest

        url = DBSession.query(Url).filter_by(id=db_id).one_or_none()
        if url is None:
            raise HttpNotFound()

        return url.url


db = DB()


class ApiV1(JsonPatchControllerMixin):

    @json
    def version(self):
        return {
            'version': urlShortener.__version__
        }


class Root(RestController):

    def _find_handler(self, remaining_paths):
        if len(remaining_paths) > 0:
            return self.resolve, remaining_paths
        return super()._find_handler(remaining_paths)

    @template('index.mak')
    def get(self):
        return dict()  # Q : Why a empty dict is returned????

    @template('successfully.mak')
    def post(self):
        return dict(hash_id =db.store(context.form.get('url')))

    @text
    def resolve(self, hexstring):
        raise HttpFound(db.resolve(hexstring))


if __name__ == '__main__':
    from nanohttp import quickstart, configure
    configure()
    try:
        quickstart(Root())
    except KeyboardInterrupt:
        print('CTRL+C just pressed')

