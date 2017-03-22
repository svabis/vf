#!/usr/bin/python
# -*- coding: utf-8 -*-
import smtplib

def send_email(recipient, body, code):
    import smtplib

    gmail_user = 'info@vfabrika.lv'
    gmail_pwd = 'fabrika2017'
    FROM = 'info@vfabrika.lv'
    TO = recipient if type(recipient) is list else [recipient]
#    SUBJECT = subject
#    SUBJECT = u'Pieraksta sistēma'
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: Pieraksta sistema\n\nPieraksts uz nodarbibu %s \nLai atceltu nodarbibu izmantojiet linku http://servax.zapto.org:8000/atcelt/%s/
    """ % (FROM, ", ".join(TO), TEXT, code)
#    """ % (FROM, ", ".join(TO), SUBJECT, TEXT, code)
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
