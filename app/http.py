import urllib3


class Http(object):
    def __init__(self, url):
        self.http = urllib3.PoolManager()
        self.url = url

    def getConnection(self):
        return self.http.request('GET', self.url)

    def postConnection(self, url, fields):
        http = self.http.request('POST', url, headers={
                                 'Content-Type': 'application/json'}, body=fields)
        return http.data

    def getData(self):
        return self.getConnection().data
