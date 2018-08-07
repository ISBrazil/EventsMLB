import imaplib
import smtplib

class Email(object):

    def __init__(self, account, passwd):
        self._account = account
        self._passwd = passwd

    def connectEmail(self):
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(self._account, self._passwd)
        mail.list()
        mail.select()

        return mail

    def connectSMTP(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(self._account, self._passwd)

        return server

    def sendEmaiil(self, emailTo, subject, text):
        try:
            server = Email.connectSMTP(self)

            BODY = '\r\n'.join(['To: %s' % emailTo,
                                'From: %s' % self._account,
                                'Subject: %s' % subject,
                                '', text])

            server.sendmail(self._account, [emailTo], BODY.encode('cp1252'))

            server.quit()
            return "OK"
        except:
            return "Error"
            raise