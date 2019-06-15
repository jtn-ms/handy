import imaplib
import email

import smtplib, ssl
import datetime

from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

import os,sys
import getpass
def send_mail(sender='secretolzs@yandex.com', passwd="Aireoqkwkrolzs",
              receivers=['delivery.olzs@yandex.com'], files=None,subject="Report",
              server='smtp.yandex.com',port=587,smode=False):
    if os.path.exists('/tmp/mail.outbox'):
        with open('/tmp/mail.outbox','r') as file:
            sender,passwd,receivers = [line for line in file]
    elif not smode:
        sender = raw_input("Sender: ") if sys.version_info[0] == 2 else input("Sender:")
        passwd = getpass.getpass()
        receivers = raw_input("Receivers: ") if sys.version_info[0] == 2 else input("Receivers:")
    if isinstance(receivers,str) and "," in receivers:receivers= receivers.split(",")
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
        print("Successfully Uploaded!")
        # saving incredentials
        with open('/tmp/mail.outbox','w') as file:
            file.writelines(['%s\n'%sender,
                             '%s\n'%passwd,
                             '%s\n'%(','.join(receivers))])
    except Exception as e:
        return False
    return True

def read_email(server_domain="imap.yandex.com",\
               usrname="delivery.olzs@yandex.com",\
               password="lqqEo&zb",smode=False):
           
    if os.path.exists('/tmp/mail.inbox'):
        with open('/tmp/mail.inbox','r') as file:
            usrname,password = [line for line in file]
    elif not smode:
        usrname = raw_input("Receiver: ") if sys.version_info[0] == 2 else input("Receiver:")
        password = getpass.getpass()
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
                    print(" Downloaded %s Successfully!"%msg['subject'])
                with open('/tmp/mail.inbox','w') as file:
                    file.writelines(['%s\n'%usrname,
                                    '%s\n'%password])
                return len(id_list),msg['from'],msg['subject']
    except Exception as e: pass
    return None,None,None