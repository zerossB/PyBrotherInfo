from app.http import Http
from app.device.status import DeviceStatus
from app.device.information import DeviceInformation


def main():
    scrap = DeviceStatus("192.168.22.95")
    print(scrap.getDeviceStatus())
    print(scrap.getTonerLevel())
    print(scrap.getDeviceLocalization())
    print(scrap.getDeviceContact())

    infos = DeviceInformation("192.168.22.95")
    infos.getAllInformation()


if __name__ == "__main__":
    main()
