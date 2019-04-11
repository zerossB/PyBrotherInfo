import urllib3
import json


class Http(object):
    def __init__(self):
        self.http = urllib3.PoolManager()

    def getConnection(self, url):
        return self.http.request('GET', url)

    def postConnection(self, url, fields):
        fields = json.dumps(fields)
        http = self.http.request('POST', url, headers={
                                 'Content-Type': 'application/json'}, body=fields)
        return http
