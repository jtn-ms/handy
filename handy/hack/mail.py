import imaplib
import email

import smtplib, ssl
import datetime

from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

def send_mail(sender='secretolzs@yandex.com', passwd="Aireoqkwkrolzs",
              receivers=['delivery.olzs@yandex.com'], files=None,subject="Report",
              server='smtp.yandex.com',port=587):
    assert(isinstance(receivers, list))

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = COMMASPACE.join(receivers)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText("this report is classified."))
    # patching
    for f in files or []:
        with open(f, "rb") as file:
            part = MIMEApplication(
                file.read(),
                Name=basename(f) 
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)
    # sending
    try:
        smtp = smtplib.SMTP(server,port)
        smtp.starttls()
        smtp.login(sender, passwd)
        smtp.sendmail(sender, receivers, msg.as_string())
        smtp.close()
    except Exception as e:
        return False
    return True

def read_email(server_domain="imap.yandex.com",\
               usrname="delivery.olzs@yandex.com",\
               password="lqqEo&zb"):
    try:
        mail = imaplib.IMAP4_SSL(server_domain)
        mail.login(usrname, password)
        mail.list()
        # Out: list of "folders" aka labels in gmail.
        mail.select("inbox") # connect to inbox.
        result, data = mail.search(None, "ALL")

        ids = data[0] # data is a list.
        id_list = ids.split() # ids is a space separated string
        latest_email_id = id_list[-1] # get the latest

        # fetch the email body (RFC822) for the given ID
        result, data = mail.fetch(latest_email_id, "(RFC822)") 

        raw_email = data[0][1] # here's the body, which is raw text of the whole email
        # including headers and alternate payloads
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1])
                if len(msg.get_payload()) > 1: 
                    attachment = msg.get_payload()[1]
                    with open(msg['subject'], 'wb') as file:
                        file.write(attachment.get_payload(decode=True))
                return len(id_list),msg['from'],msg['subject']
    except Exception as e: pass
    return None,None,None