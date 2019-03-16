import falcon


class InfoResource:
    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        response.media = {'app': 'endex'}


app = falcon.API()
app.add_route('/', InfoResource())
