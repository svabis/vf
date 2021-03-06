#!/usr/bin/python2
# -*- coding: utf-8 -*-

# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

from datetime import datetime
from datetime import timedelta

# DST
def dst(time):
    import calendar
    import datetime
    date = time.date()
    year = date.year

    dst_start = max(week[-1] for week in calendar.monthcalendar(year, 10))
    dst_end   = max(week[-1] for week in calendar.monthcalendar(year, 3))
    date_dst_start = datetime.date(year, 10, dst_start)
    date_dst_end = datetime.date(year, 3, dst_end)

    if date_dst_end <= date <= date_dst_start:
        return 3
    else:
        return 2

# !!!!! PIETEIKUMA APSTIPRINAJUMS !!!!!
def send_email(recipient, nodarb, timedate, code_uuid):
    # Define these once; use them twice!
    strFrom = 'info@vfabrika.lv'
    strTo = recipient

    new_time = timedate + timedelta(hours=dst(timedate))
    time = new_time.strftime("%Y/%m/%d %H:%M")

    code = 'http://pieraksts.vfabrika.lv/atcelt/' + str(code_uuid) + '/'

# Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = u'"Veselības Fabrika" pieraksts'
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
    content = u'<b><p>Paldies par veikto rezervāciju uz nodarbību – <i>' + time + ', ' + nodarb + u'</i></b></p><br><p>Rezervācijas atcelšanai lūdzam izmantot šo saiti:<br>' + code + u'</p><br><p>Jūsu sporta klubs <b><i> “</i>Veselības Fabrika<i>”</i></b></p><img src="cid:image1">'
    msgText = MIMEText(content.encode('utf-8'), 'html','utf-8')
    msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
    fp = open('/pieraksts/static/logo.jpg', 'rb')
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



# ===================================================================================================
# !!!!! ATCELSHANA !!!!!
def send_cancel(recipient, datums, nos):
    # Define these once; use them twice!
    strFrom = 'info@vfabrika.lv'
    strTo = recipient

    new_time = datums + timedelta(hours=dst(datums))

    time = new_time.strftime("%Y/%m/%d %H:%M")

# Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = u'"Veselības Fabrika" pieraksts'
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
    fp = open('/pieraksts/static/logo.jpg', 'rb')
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


# ===================================================================================================
# !!!!! ATGĀDINĀJUMS !!!!!
def send_remind(recipient, nodarb, timedate, code_uuid):
    # Define these once; use them twice!
    strFrom = 'info@vfabrika.lv'
    strTo = recipient

#    new_time = timedate + timedelta(hours=3)
    new_time = timedate + timedelta(hours=dst(timedate))
    time = new_time.strftime("%d/%m/%Y %H:%M")

    code = 'http://pieraksts.vfabrika.lv/atcelt/' + str(code_uuid) + '/'

# Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = u'"Veselības Fabrika" atgādinājums'
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
    content = u'<p>Sveiki! Atgādinām, ka esat pieteicies/kusies uz nodarbību (<b>' + time + ', ' + nodarb + u'</b> ), Gaidīsim, Jūs, "Veselības Fabrikā"!</p><p>Ja tomēr pārdomāsiet, klikšķiniet uz šo saiti, lai atteiktos no nodarbības ( <b>' + code + u'</b> ).</p><p>Jūsu sporta klubs <b><i> “</i>Veselības Fabrika<i>”</i></b></p><img src="cid:image1">'
    msgText = MIMEText(content.encode('utf-8'), 'html','utf-8')
    msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
    fp = open('/pieraksts/static/logo.jpg', 'rb')
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




















# SORRY
# ===================================================================================================
def send_sorry(recipient, nodarb, timedate, code_uuid):
    # Define these once; use them twice!
    strFrom = 'info@vfabrika.lv'
    strTo = recipient

#    new_time = timedate + timedelta(hours=3)
    new_time = timedate + timedelta(hours=dst(timedate))
    time = new_time.strftime("%d/%m/%Y %H:%M")

    code = 'http://pieraksts.vfabrika.lv/atcelt/' + str(code_uuid) + '/'

# Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = u'Pieraksta sistēma, Paziņojums par kļūdu.'
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
    content = u'<p>Sveiki! Atvainojamie par ieprikš kļūdaini izsūtītu e-pastu.</p><p>30/10 visas nodarbības notiek pēc grafika. Atvainojamies par sagādātajām neērtībām.<p>Jūsu sporta klubs <b><i> “</i>Veselības Fabrika<i>”</i></b></p><img src="cid:image1">'
    msgText = MIMEText(content.encode('utf-8'), 'html','utf-8')
    msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
    fp = open('/pieraksts/static/logo.jpg', 'rb')
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

