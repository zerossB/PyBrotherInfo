from app.http import Http

from bs4 import BeautifulSoup


class DeviceInformation(object):
    def __init__(self, url):
        self.httpd = Http()
        data = self.httpd.getConnection(
            "http://"+url+"/general/information.html?kind=item").data
        self.data = BeautifulSoup(data, "html.parser")
        self.keys = []
        self.values = []

    def getAllInformation(self):
        dt = self.data.findAll('dt')
        dd = self.data.findAll('dd')
        for item in dt:
            self.keys.append(item.text.replace('*', ''))
        for item in dd:
            self.values.append(item.text)
        for item in zip(self.keys, self.values):
            print(item)
