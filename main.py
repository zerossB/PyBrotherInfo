from app.http import Http
from app.device.status import DeviceStatus
from app.device.information import DeviceInformation
from app.mail import Mail
from app.mail.template import Template

from app import settings as st


def main():
    template = Template()

    for impressora in st.DEVICES_IP:
        infos = DeviceInformation(impressora)
        status = DeviceStatus(impressora)

        print(status.getDeviceStatus())

        if status.getDeviceStatus()[0] != "ok":
            for ti in st.EMAILS_TI:
                mail = Mail()
                mail.sendHTML(
                    to=ti,
                    subject="Informações Impressora " + status.getDeviceLocalization(),
                    message=template.renderEmail(infos, status)
                )

        print("Impressora ok " + status.getDeviceLocalization())


if __name__ == "__main__":
    main()
