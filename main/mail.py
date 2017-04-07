#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage


# !!!!! PIETEIKUMA APSTIPRINAJUMS !!!!!
def send_email(recipient, nodarb, timedate, code_uuid):
    # Define these once; use them twice!
    strFrom = 'info@vfabrika.lv'
    strTo = recipient
    time = str(timedate)
    code = 'http://servax.zapto.org:8000/atcelt/' + str(code_uuid) + '/'

# Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = u'Pieraksta sistēma'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
    content = u'<b><p>Paldies par veikto rezervāciju uz nodarbību – <i>' + nodarb + ' , ' + time  + u'</i></b></p><p>Rezervācijas atcelšanai lūdzam izmantot šo saiti:<br>' + code + u'</p><p>Jūsu sporta klubs <b><i> “</i>Veselības Fabrika<i>”</i></b></p><img src="cid:image1">'
    msgText = MIMEText(content.encode('utf-8'), 'html','utf-8')
    msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
    fp = open('vfabrika.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

# Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

# Send the email (SMTP authentication is required)
    import smtplib
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(strFrom, 'fabrika2017')
    smtp.sendmail(strFrom, strTo, msgRoot.as_string())
    smtp.quit()





# !!!!! ATCELSHANA !!!!!
def send_cancel(recipient, datums, nos):
    # Define these once; use them twice!
    strFrom = 'info@vfabrika.lv'
    strTo = recipient
    time = str(datums)
#    code = 'http://servax.zapto.org:8000/atcelt/' + str(code_uuid) + '/'

# Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = u'Pieraksta sistēma'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below

    content = u'<p><b>' + time + u' paredzētā nodarbība ' + nos + u' atceļas.</b></p><p> Aicinām pieteikties uz citu nodarbību vai vingrot mūsu trenažieru zālē.</p><p>Atvainojamies par neērtībām.</p><p>Jūsu sporta klubs <b><i> “</i>Veselības Fabrika<i>”</i></b></p><img src="cid:image1">'
    msgText = MIMEText(content.encode('utf-8'), 'html','utf-8')
    msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
    fp = open('vfabrika.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

# Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

# Send the email (SMTP authentication is required)
    import smtplib
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(strFrom, 'fabrika2017')
    smtp.sendmail(strFrom, strTo, msgRoot.as_string())
    smtp.quit()
