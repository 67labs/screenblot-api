from tornado.web import RequestHandler, asynchronous
from tornado.gen import coroutine
from tornado.escape import url_unescape
from tornado.concurrent import return_future
from selenium import webdriver

from screenblot import settings


class ScreenshotHandler(RequestHandler):
    @return_future
    def screenshot(self, url, width, height, callback):
        driver = webdriver.PhantomJS(settings.PHANTOM_BIN)
        driver.set_window_size(width, height)
        driver.get(url)
        # Temporarily just return an image
        # driver.save_screenshot('screen.png')
        callback(driver.get_screenshot_as_png())

    @asynchronous
    @coroutine
    def get(self):
        url = url_unescape(self.get_argument('url'))
        width = int(self.get_argument('width', 1280))
        height = int(self.get_argument('height', 720))

        data = yield self.screenshot(url, width, height)

        self.set_header("Content-Type", "image/png")
        self.write(data)
