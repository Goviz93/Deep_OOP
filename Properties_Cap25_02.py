"""
    Python 3: Deep Dive (Part 4 - OOP)
    Chap. 25 Read Only and Computed Properties - Coding


"""


from urllib.request import urlopen
from time import perf_counter

class WebPage:

    def __init__(self, url):
        self.url = url
        self._page = None
        self._load_time_secs = None
        self._page_size = None

    @property
    def url(self):
        return self._url


    @url.setter
    def url(self, value):
        self._url = value
        self._page = None


    #read only property
    @property
    def page(self):
        if self._page is None:
            self.download_page()
        return self._page


    # read only property
    @property
    def page_size(self):
        if self._page_size is None:
            self.download_page()
        return self._page_size


    # read only property
    @property
    def time_elapsed(self):
        if self._page is None:
            self.download_page()
        return self._load_time_secs

    def download_page(self):
        self._page_size = None
        self._load_time_secs = None
        start_time = perf_counter()
        with urlopen(self.url) as web:
            self._page = web.read()
        end_time = perf_counter()
        self._page_size = len(self._page)
        self._load_time_secs = end_time - start_time


if __name__ == '__main__':

    URLS = [
        "https://www.youtube.com",
        "https://www.python.org",
        "https://www.google.com.mx/?hl=es-419"
    ]

    for u in URLS:
        webApp = WebPage(u)
        print(webApp.url)
        #print(webApp.page)
        print(format(webApp.page_size, "_"))
        print(webApp.time_elapsed)