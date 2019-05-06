from app.http import Http

from bs4 import BeautifulSoup


class DeviceStatus(object):
    def __init__(self, url):
        self.httpd = Http()
        data = self.httpd.getConnection(
            "http://"+url+"/general/status.html").data
        self.data = BeautifulSoup(data, "html.parser")

    def getTonerLevel(self):
        toner = self.data.find('img', {'class': 'tonerremain'})
        return toner['height']

    def getDeviceLocalization(self):
        localization = self.data.find('li', {'class': 'location'})
        return localization.text[9:]

    def getDeviceContact(self):
        localization = self.data.find('li', {'class': 'contact'})
        return localization.text

    def getDeviceStatus(self):
        status = self.data.find('span', {'class': 'moni'})['class'][1]
        text = self.data.find('span', {'class': 'moni'}).text

        if "Ok" in status:
            status = "ok"
        elif "Warning" in status:
            status = "warning"
        elif "Error" in status:
            status = "error"
        else:
            status = "etc"

        return status, text.rstrip()
