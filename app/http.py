import urllib3


class Http(object):
    def __init__(self, url):
        self.http = urllib3.PoolManager()
        self.url = url

    def connect(self):
        return self.http.request('GET', self.url)

    def getData(self):
        return self.connect().data
