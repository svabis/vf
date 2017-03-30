#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sys
import smtplib
import email
import re

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendmail(firm, fromEmail, to, template, subject, date):
    with open(template) as template_file:
        message = template_file.read()

    message = re.sub(r"{{\s*firm\s*}}", firm, message)
    message = re.sub(r"{{\s*date\s*}}", date, message)
    message = re.sub(r"{{\s*from\s*}}", fromEmail, message)
    message = re.sub(r"{{\s*to\s*}}", to, message)
    message = re.sub(r"{{\s*subject\s*}}", subject, message)

    msg = MIMEMultipart("alternative")
    msg.set_charset("utf-8")

    msg["Subject"] = subject
    msg["From"] = fromEmail
    msg["To"] = to

    #Read from template
    html = message[message.find("html:") + len("html:"):message.find("text:")].strip()
    text = message[message.find("text:") + len("text:"):].strip()

    part1 = MIMEText(html, "html")
    part2 = MIMEText(text, "plain")

    msg.attach(part1)
    msg.attach(part2)

#    if True:
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(fromEmail, 'fabrika2017')
#        server = smtplib.SMTP("10.0.0.5")
        server.sendmail(fromEmail, [to], msg.as_string())
        return 0
    except Exception as ex:
        #log error
        #return -1
        #debug
        raise ex
    finally:
        server.quit()

if __name__ == "__main__":
    #debug
    sys.argv.append("V-FABRIKA")
#    sys.argv.append("newsletter@example.cz")
#    sys.argv.append("subscriber@example.com")
    sys.argv.append("info@vfabrika.lv")
    sys.argv.append("fizmats@inbox.lv")
    sys.argv.append("vest")
    sys.argv.append("This is subject")
    sys.argv.append("This is date")


    if len(sys.argv) != 7:
        exit(-2)

    firm = sys.argv[1]
    fromEmail = sys.argv[2]
    to = sys.argv[3]
    template = sys.argv[4]
    subject = sys.argv[5]
    date = sys.argv[6]

    exit(sendmail(firm, fromEmail, to, template, subject, date))

# ====================================================================================================================

def send_email(recipient, subject, body):
    import smtplib

    gmail_user = 'info@vfabrika.lv'
    gmail_pwd = 'fabrika2017'
    FROM = 'info@vfabrika.lv'
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

#send_email('fizmats@inbox.lv', 'Mail Subject', 'Teksts')
#send_email('lspjurmala2013@gmail.com', 'Mail Subject', 'Teksts')
#send_email('kristine@vfabrika.lv', 'Mail Subject', 'Teksts')
