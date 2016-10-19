import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpserver

from screenblot import settings
from screenblot.handler import ScreenshotHandler


def build_app():
    app = tornado.web.Application(
        [
            (r'/api/v1/screenshot/', ScreenshotHandler),
        ],
        **settings.TORNADO_SETTINGS
    )
    return app


def main():
    tornado.options.parse_command_line()
    try:
        app = build_app()
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.bind(settings.TORNADO_SERVER_PORT)
        http_server.start(settings.TORNADO_PROCESSES)
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()
