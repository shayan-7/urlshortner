import unittest

from restfulpy.principal import JwtPrincipal
from restfulpy.testing import FormParameter

from urlShortener.tests.helpers import WebTestCase, As
from urlShortener.models import Member


class AuthenticationTestCase(WebTestCase):

    @classmethod
    def mockup(cls):
        cls.application.insert_mockup()

    @classmethod
    def update_user(cls, email, attributes: dict):
        user = cls.session.query(Member).filter(Member.email == email).one()
        for k, v in attributes.items():
            setattr(user, k, v)
        cls.session.commit()

    def test_login(self):
        # Login, White box
        result, meta = self.request(
            As.anonymouse, 'POST', '/apiv1/sessions',
            params=[
                FormParameter('email', 'god@example.com'),
                FormParameter('password', '123456')
            ]
        )
        self.assertIn('token', result)
        principal = JwtPrincipal.load(result['token'])
        self.assertIn('sessionId', principal.payload)
        self.assertDictContainsSubset(principal.payload, {
            'id': 1,
            'email': 'god@example.com',
            'name': 'God'
        })

        # Request a protected resource
        self.request(As.user, 'GET', '/', headers={'Authorization': f'Bearer {result["token"]}'})

        # Request a protected resource without token
        self.request(As.user, 'GET', '/', expected_status=401)

    def test_token_info(self):
        # Issue 86
        result, meta = self.request(
            As.anonymouse, 'POST', '/apiv1/sessions',
            params=[
                FormParameter('email', 'user1@example.com'),
                FormParameter('password', '123456')
            ]
        )
        principal = JwtPrincipal.load(result['token'])
        self.assertIn('sessionId', principal.payload)
        self.assertDictContainsSubset(principal.payload, {
            'id': 2,
            'email': 'user1@example.com',
            'name': 'test user 1',
            'specialityId': 1
        })

    def test_login_errors(self):
        self.request(
            As.anonymouse, 'POST', '/apiv1/sessions',
            params=[
                FormParameter('email', 'invaliduser@example.org'),
                FormParameter('password', 'invalidPassword')
            ],
            expected_status=400
        )

        # Without parameters
        self.request(
            As.anonymouse, 'POST', '/apiv1/sessions',
            params=[
                FormParameter('email', 'invaliduser@example.org'),
            ],
            expected_status=400
        )

        # With wrong password
        self.request(
            As.anonymouse, 'POST', '/apiv1/sessions',
            params=[
                FormParameter('email', 'god@example.com'),
                FormParameter('password', 'invalidPassword')
            ],
            expected_status=400
        )

        # By deactivated user
        email = 'user1@example.com'
        self.update_user(email, dict(is_active=False))
        ___, response_headers = self.request(
            As.anonymouse, 'POST', '/apiv1/sessions',
            params=[
                FormParameter('email', email),
                FormParameter('password', '123456')
            ],
            expected_status=409
        )
        self.assertIn('X-Reason', response_headers)
        self.assertEqual(response_headers['X-Reason'], 'user-deactivated')
        self.update_user(email, dict(is_active=True))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
