import unittest

from bddrest.authoring import then, response

from urlshortener.tests.helpers import BDDTestClass


class AuthTestCase(BDDTestClass):

    def test_auth(self):

        call = dict(
            title='POST',
            description='',
            url='/auth',
            verb='POST',
        )
        with self.given(**call):
            then(response.status_code == 200)

        call = dict(
            title='GET',
            description='',
            url='/auth?state=yZlnAejV1H0cd4cJ8jelnavTsvePuf&code=4/AAACM08NCbCv97ix1FwQK4GaauRUMSG9li3ZNCTRzretKoV_dkQ9roMsL-iYc0crHAQIB9KE9eQqfMH-nS6LxgU&scope=https://www.googleapis.com/auth/userinfo.email+https://www.googleapis.com/auth/plus.me#',
            verb='GET',
        )
        with self.given(**call):
            then(response.status_code == 200)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
