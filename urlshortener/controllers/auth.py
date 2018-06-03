from os.path import join, dirname, abspath
from urllib.request import Request, urlopen


from nanohttp import RestController, text, HttpFound, context, json
import google_auth_oauthlib.flow

client_secret_file = join(abspath(join(dirname(__file__), '..')),
                          'basedata/client_secrets.json')


class Auth(RestController):

    @json
    def get(self):

        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            client_secret_file,
            scopes=context.query_string.get('scope'),
            state=context.query_string.get('state')
        )

        flow.redirect_uri = 'http://localhost:8080/auth'
        flow.fetch_token(
            authorization_response=
            'https://www.googleapis.com/oauth2/v1/userinfo.profile',
            code=context.query_string.get('code')
        )

        credentials = flow.credentials

        if credentials is not None:
            headers = {'Authorization': 'OAuth ' + credentials.token}
            req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
                          None, headers)

            response = urlopen(req)
            json_response = response.read().decode("utf-8")

        return json_response

    @text
    def post(self):

        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            client_secret_file,
            scopes=['https://www.googleapis.com/auth/userinfo.profile']
        )

        flow.redirect_uri = 'http://localhost:8080/auth'
        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true')

        raise HttpFound(authorization_url)
