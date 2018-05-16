from nanohttp import Controller, RestController, context, json, html, text, HttpFound
from hashids import Hashids

list_url = []
hashids = Hashids(salt='this is my salt')

def search_in_list(url):
    if url in list_url:
        return True
    else:
        return False

class UrlShortener(RestController):


    @text
    def post(self, url: str=None):
        url = context.form.get('url')
        print('url entry: ', url)

        is_exist = search_in_list(url)
        print(f'Search result: {is_exist}')

        if is_exist == True:
            key = list_url.index(url)
        else:
            key = len(list_url)
            list_url.append(url)

        print('key: ', key)
        hash_id = hashids.encode(key)
        yield f'urlshortener.com\{hash_id}'
        #print(*list_url, sep='\n')

    @html
    def get(self):
        yield """
        <html><head><title>nanohttp Demo</title></head><body>
        <p>mohammad</p>
        </body></html>
        """

class Root(Controller):
    urlshortener=UrlShortener()

    @html
    def index(self):
        yield """
        <html><head><title>nanohttp Demo</title></head><body>
        <form method="POST" action="/urlshortener">
            <input type="text" name="url" />
            <input type="submit" value="url" />
        </form>
        </body></html>
        """

