from os.path import join, dirname, abspath
from urllib.request import Request, urlopen


from nanohttp import RestController, text, HttpFound, context, json, settings
import google_auth_oauthlib.flow

client_secret_file = join(abspath(join(dirname(__file__), '..')),
                          'basedata/client_secrets.json')


class Auth(RestController):

    @json
    def get(self):

        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            client_secret_file,
            scopes=context.query_string.get('scope'),
            state=context.query_string.get('state'),
            redirect_uri=settings.auth_url
        )

        flow.fetch_token(
            authorization_response=settings.oauth_scope,
            code=context.query_string.get('code'),
        )

        if flow.credentials is not None:
            headers = {'Authorization': 'OAuth ' + flow.credentials.token}
            req = Request(settings.oauth_url_api, None, headers)

            response = urlopen(req)

        return response.read().decode("utf-8")

    @text
    def post(self):

        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            client_secret_file,
            scopes=[settings.oauth_scope],
            redirect_uri=settings.auth_url
        )

        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true')

        raise HttpFound(authorization_url)
