import falcon

from . import cx


class InfoResource:
    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        response.media = {'app': 'endex'}


def get_app_api():
    app = falcon.API()
    app.add_route('/', InfoResource())
    return app


def get_app():
    print('[get_app] init db connection')
    # db.init(get_db_config())
    cx.get()
    print('[get_app] returning application')
    return get_app_api()
