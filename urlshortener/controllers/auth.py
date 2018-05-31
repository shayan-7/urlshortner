from os.path import join, dirname, abspath

from nanohttp import RestController, text, HttpFound, contexts, context
from oauth2client.client import OAuth2WebServerFlow
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
import requests
import httplib2

client_secret_file = join(join(abspath(join(dirname(__file__), '..')),
                               'basedata'), 'client_secrets.json')

flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    client_secret_file,
    scopes=['https://www.googleapis.com/auth/userinfo.profile']
)

flow.redirect_uri = 'http://localhost:8080/auth'

authorization_url, state = flow.authorization_url(
    access_type='offline',
    include_granted_scopes='true')


class Auth(RestController):

    @text
    def get(self):
        query_string_state = context.query_string.get('state')
        query_string_code = context.query_string.get('code')
        query_string_scope = context.query_string.get('scope')
        query_string_scope = 'https://www.googleapis.com/auth/userinfo.profile'

        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            client_secret_file,
            scopes=query_string_scope,
            state=query_string_state)

        flow.redirect_uri = 'http://localhost:8080/auth'
        flow.fetch_token(
            authorization_response=
            'https://www.googleapis.com/oauth2/v1/userinfo.profile',
            code=query_string_code
        )

        credentials = flow.credentials
        # revoke = requests.post('https://www.googleapis.com/oauth2/v1/userinfo',
        #                        params={'token': credentials.token},
        #                        headers={'content-type': 'application/x-www-form-urlencoded'}
        #                        )

        if credentials is not None:
            # http = httplib2.Http()
            # http = credentials.authorize(http)
            drive = build('userinfo.profile', 'v1', credentials=credentials)

        return dict()

    @text
    def post(self):
        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true')

        raise HttpFound(authorization_url)
