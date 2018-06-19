import requests
import ast
import json as json_library
from os.path import join, dirname, abspath

from restfulpy.principal import JwtPrincipal

from restfulpy.orm import DBSession
from nanohttp import RestController, text, HttpFound, context, json, settings,\
    HttpForbidden, HttpNotFound, HttpBadRequest
import google_auth_oauthlib.flow

from urlshortener.models.member import Member

client_secret_file = join(abspath(join(dirname(__file__), '..')),
                          'basedata/client_secrets.json')
json_data = open(client_secret_file).read()
client_secret_data = json_library.loads(json_data)['web']


class Auth(RestController):

    @json
    def get(self):

        if(context.query_string.get('code') is None) or \
                (client_secret_data['client_id'] is None) or \
                (client_secret_data['client_secret'] is None):
            raise HttpBadRequest

        body_token = dict()
        body_token['grant_type'] = 'authorization_code'
        body_token['code'] = context.query_string.get('code')
        body_token['client_id'] = client_secret_data['client_id']
        body_token['redirect_uri'] = settings.redirect_uri_auth
        body_token['client_secret'] = client_secret_data['client_secret']

        response_token = requests.post(
            settings.auth_google_uri_token,
            body_token
        )

        if response_token.status_code != 200:
            raise HttpForbidden()

        response_get_profile = requests.get(
            settings.oauth_url_google_api,
            headers={
                'Authorization':
                    'OAuth ' +
                    json_library.loads(response_token.text)['access_token']
            }
        )

        if response_get_profile.status_code != 200:
            raise HttpNotFound()

        profile = json_library.loads(response_get_profile.text)

        if 'refresh_token' in response_token.text:
            member = Member(
              given_name=profile['given_name'],
              family_name=profile['family_name'],
              email=profile['email'],
              google_access_token=
              json_library.loads(response_token.text)['access_token'],
              google_refresh_token=
              json_library.loads(response_token.text)['refresh_token']
            )
            DBSession.add(member)
            DBSession.commit()

        return dict(authorization=JwtPrincipal(profile).dump().decode("utf-8"))

    @text
    def post(self):

        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            client_secret_file,
            scopes=[settings.oauth_google_scope],
            redirect_uri=settings.redirect_uri_auth
        )

        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true')

        raise HttpFound(authorization_url)
