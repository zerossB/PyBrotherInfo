from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import app.settings as st

# Based: https://gist.github.com/dtanham/11326557


class Mail(object):
    def __init__(self):
        if st.EMAIL_HOST == "" or st.EMAIL_PORT:
            raise NotImplementedError(
                "EMAIL_HOST ou EMAIL_PORT não configurados no settings.py")
        self.server = smtplib.SMTP(
            st.EMAIL_HOST, st.EMAIL_PORT
        )

    def send(self, to, subject, message, content_type):
        msg = MIMEMultipart()
        msg['From'] = st.EMAIL_HOST_USER
        msg['To'] = to
        msg['Subject'] = subject

        content = MIMEText(message, content_type)
        msg.attach(content)

        try:
            self.server.login(st.EMAIL_HOST_USER, st.EMAIL_HOST_PASS)
            if st.EMAIL_USE_TLS:
                self.server.starttls()
            self.server.sendmail(
                st.EMAIL_HOST_USER, to, msg.as_string()
            )
        except Exception as ex:
            print(ex)
        finally:
            self.server.quit()

    def sendHTML(self, to, subject, message):
        return self.send(to, subject, message, "html")

    def sendText(self, to, subject, message):
        return self.send(to, subject, message, "plain")
