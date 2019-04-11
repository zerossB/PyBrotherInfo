from app.http import Http
from app.devicestatus import DeviceStatus
from app.deviceinformation import DeviceInformation


def main():
    httpd = Http()
    # scrap = DeviceStatus(httpd.getConnection(
    #     "http://192.168.22.95/general/status.html").data)
    # print(scrap.getDeviceStatus())
    # print(scrap.getTonerLevel())
    # print(scrap.getDeviceLocalization())
    # print(scrap.getDeviceContact())

    infos = DeviceInformation(httpd.getConnection(
        "http://192.168.22.95/general/information.html?kind=item").data)
    infos.getAllInformation()


if __name__ == "__main__":
    main()
