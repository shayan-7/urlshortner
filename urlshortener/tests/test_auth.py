import unittest
from contextlib import contextmanager

from bddrest.authoring import then, response
from restfulpy.testing.mockup import http_server
from urlshortener.tests.helpers import MockupApplication, document_directory
from nanohttp import RestController, settings, json, context, HttpBadRequest, \
    HttpUnauthorized

from urlshortener.tests.helpers import BDDTestClass


class Token(RestController):
    @json
    def post(self):
        if '4/AAA' in context.form.get('code'):
            return dict(
                access_token='ya29.GlzVBYKNxVGGMl6euQ6U-_QIhylTdqoYXxW3MHOXL7\
                r6WmO2xx_wkBht6TT6OIP0eoDjcQIm3Y6JXmAExohf7GU3xuhs6cF9EcL5DbT\
                owmmH-nBlVE6Uop2IftiFtQ',
                refresh_token='1/Yn_cvrK7qeJ9yNQcl77dHNqrqO1Q_ySU5MhibfXkvOo3\
                vZct44-X5rUdvCRM9jJE'
            )
        elif '5/AAA' in context.form.get('code'):
            return dict(
                access_token='ya30.GlzVBYKNxVGGMl6euQ6U-_QIhylTdqoYXxW3MHOXL7\
                r6WmO2xx_wkBht6TT6OIP0eoDjcQIm3Y6JXmAExohf7GU3xuhs6cF9EcL5DbT\
                owmmH-nBlVE6Uop2IftiFtQ'
            )
        else:
            raise HttpBadRequest()


class Profile(RestController):

    @json
    def get(self):
        access_token = context.environ.get('HTTP_AUTHORIZATION')

        if 'ya29.GlzVBYKNxVGGMl6euQ6U' in access_token:
            return {
                'id': '105202566366011957392',
                'email': 'mohammadsheikhian70@gmail.com',
                'verified_email': True,
                'name': 'Mohammad Sheikhian',
                'given_name': 'Mohammad',
                'family_name': 'Sheikhian',
                'link': 'https://plus.google.com/105202566366011957392',
                'picture': 'https://lh4.googleusercontent.com/-9gnVQNZquf%20g'
                           '/AAAAAAAAAAI/AAAAAAAAAD0/g4AAMkzYkpc/photo.jpg',
                'gender': 'male',
                'locale': 'fa'
            }
        else:
            raise HttpUnauthorized()


class Root(RestController):
    token = Token()
    profile = Profile()


@contextmanager
def oauth_mockup_server(root_controller):
    app = MockupApplication('root', root_controller)
    with http_server(app) as (server, url):
        settings.merge(f'''
            tokenizer:
              url: {url}
        ''')
        yield app


class AuthTestCase(BDDTestClass):

    def test_auth_post(self):

        call = dict(
            title='POST',
            description='Create redirect url',
            url='/auth',
            verb='POST',
            autodoc=f'{document_directory}/auth_post.md'
        )
        with self.given(**call):
            then(response.status_code == 302)

    def test_auth_get(self):
        with oauth_mockup_server(Root()):
            settings.mockup_server_url = settings.tokenizer['url']
            settings.auth_google_uri_token = f'{settings.mockup_server_url}' \
                                             f'/token'
            settings.oauth_url_google_api = f'{settings.mockup_server_url}' \
                                            f'/profile'

            call = dict(
                title='GET',
                description='Key value error code or state or scope',
                url='/auth',
                verb='GET',
                query={}
            )
            with self.given(**call):
                then(response.status_code == 400)

            call = dict(
                title='GET',
                description='invalid code or state or scope',
                url='/auth',
                verb='GET',
                query={
                    'state': 'DAMDzeJImyByVNSdUOVMzy5moo77JZ',
                    'code': '_ieAH5x0_nAl45U03Iom6Ut2bcMV-oN8pYrnZtGUYKD'
                            'povHVmjpCbWu4zBdUYrLtb6JMguFf_E2tyxqLo_vo',
                    'scope': 'https://www.googleapis.com/auth/userinfo.profile'
                             ' https://www.googleapis.com/auth/plus.me '
                             'https://www.googleapis.com/auth/userinfo.email'
                }
            )
            with self.given(**call):
                then(response.status_code == 403)

            call = dict(
                title='GET',
                description='',
                url='/auth',
                verb='GET',
                query={
                    'state': 'DAMDzeJImyByVNSdUOVMzy5moo77JZ',
                    'code': '5/AAA_ieAH5x0_nAl45U03Iom6Ut2bcMV-oN8pYrnZtGU'
                            'YKDpovHVmjpCbWu4zBdUYrLtb6JMguFf_E2tyxqLo_vo',
                    'scope': 'https://www.googleapis.com/auth/userinfo.profile'
                             ' https://www.googleapis.com/auth/plus.me '
                             'https://www.googleapis.com/auth/userinfo.email'
                }
            )
            with self.given(**call):
                then(response.status_code == 404)

            call = dict(
                title='GET',
                description='',
                url='/auth',
                verb='GET',
                query={
                    'state': 'DAMDzeJImyByVNSdUOVMzy5moo77JZ',
                    'code': '4/AAA_ieAH5x0_nAl45U03Iom6Ut2bcMV-oN8pYrnZtGU'
                            'YKDpovHVmjpCbWu4zBdUYrLtb6JMguFf_E2tyxqLo_vo',
                    'scope': 'https://www.googleapis.com/auth/userinfo.profile'
                             ' https://www.googleapis.com/auth/plus.me '
                             'https://www.googleapis.com/auth/userinfo.email'
                },
                autodoc=f'{document_directory}/auth_get.md'
            )
            with self.given(**call):
                then(response.status_code == 200)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
