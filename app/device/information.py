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

        self._getAllInformation()

    def _getAllInformation(self):
        dt = self.data.findAll('dt')
        dd = self.data.findAll('dd')
        for item in dt:
            self.keys.append(item.text.replace('*', ''))
        for item in dd:
            self.values.append(item.text)

    def _getPosition(self, text):
        for index, item in enumerate(zip(self.keys, self.values)):
            if text in item[0]:
                return index

    def _replace(self, page, percent):
        pages = page.replace("pages", "")
        percents = percent.replace("(", "").replace(")", "")
        return pages, percents

    def getModelName(self):
        return self.values[self._getPosition("Model Name")]

    def getSerialNumber(self):
        return self.values[self._getPosition("Serial")]

    def getPageCouter(self):
        return self.values[self._getPosition("Page Counter")]

    def getDrumUnit(self):
        return self.values[self._getPosition("Drum Unit")]

    def getFuserUnit(self):
        pos = self._getPosition("Fuser Unit")
        pages = self.values[pos]
        percent = self.values[pos + 1]
        return self._replace(pages, percent)

    def getLaserUnit(self):
        pos = self._getPosition("Laser Unit")
        pages = self.values[pos]
        percent = self.values[pos + 1]
        return self._replace(pages, percent)

    def getTonerPercent(self):
        pos = self._getPosition("Toner")
        percent = self.values[pos]
        return percent
