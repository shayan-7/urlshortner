from nanohttp import RestController, HttpBadRequest, HttpNotFound, HttpFound, \
    text
from restfulpy.orm import DBSession
from hashids import Hashids

from urlshortener.models.urls import Url

hashids = Hashids(salt="url shortener")


class Urls(RestController):

    @text
    def get(self, hash_id):
        try:
            db_id, = hashids.decode(hash_id)
        except ValueError:
            raise HttpBadRequest()

        url = DBSession.query(Url).filter_by(id=db_id).one_or_none()
        if url is None:
            raise HttpNotFound()

        raise HttpFound(url.url)
