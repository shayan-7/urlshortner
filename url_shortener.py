from nanohttp import Controller, RestController, context, html, text, HttpFound
from hashids import Hashids

list_url = []
hashids = Hashids(salt='this is my salt')


class UrlShortener(RestController):
    @html
    def post(self):
        url = context.form.get('url')
        print('url entry: ', url)

        if url in list_url:
            key = list_url.index(url)
        else:
            key = len(list_url)
            list_url.append(url)

        print('key: ', key)
        hash_id = hashids.encode(key)
        yield f"""
        <html><head><title>Url shortener</title></head><body>
        <div style="background-color:MediumSeaGreen;color:white;padding:20px;">
        <h2 style="text-align:center;">Successfully</h2>
        <p style="text-align:center; color:black"><strong>Shortener url: http://localhost:8080/urlid/{hash_id}</strong></p>
        </div>
        </body></html>
        """


class UrlId(RestController):
    @html
    def get(self, url_id: str=None):
        print('url id: ', url_id)

        try:
            if url_id != None:
                key = hashids.decode(url_id)[0]
                print('key ', key)

                if key < len(list_url):
                    url = list_url[key]
                else:
                    url = None
            else:
                url = None
        except:
            url = None

        print('url: ', url)

        if url != None:
            if 'http://' in url:
                raise HttpFound(url)
            else:
                raise HttpFound('http://' + url)
        else:
            yield """
            <html><head><title>Url shortener</title></head><body style="padding:80px;">
            <div style="background-color:Gray;color:white;padding:20px;">
            <h1 style="text-align:center;">Can not found page</h1>
            </div>
            </body></html>
            """


class Root(Controller):
    urlshortener = UrlShortener()
    urlid = UrlId()

    @html
    def index(self):
        yield """
        <html><head><title>Url shortener</title></head><body>
        <div style="background-color:DodgerBlue;color:white;padding:20px;">
        <form method="POST" action="/urlshortener">
        <strong>Iuput url:</strong>
            <input type="text" name="url" />
            <input type="submit" value="Submit" />
        </form>
        </div>
        </body></html>
        """

