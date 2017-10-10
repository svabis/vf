#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import imaplib
import getpass
import email
import datetime

#import os

#last_date = datetime.datetime(2017, 8, 1, 00, 00)
last_date = datetime.datetime.now() - datetime.timedelta(days=2)

print last_date

# Function that processess the 'M' mailbox
def process_mailbox(M):
  # rv - 'OK'	# data - ['1 2 3']	# data[0] - '1 2 3'	# data[0].split() - 1,2,3
  rv, data = M.search(None, "ALL")
  if rv != 'OK':
      print "No messages found!"
      return

  for num in reversed(data[0].split()):
      rv, data = M.fetch(num, '(RFC822)')
      if rv != 'OK':
          print "ERROR getting message", num
          return

      msg = email.message_from_string(data[0][1])

      if msg['Subject'] == '=?utf-8?q?Pieraksta_sist=C4=93ma?=' \
        or msg['Subject'] == '=?utf-8?q?Pieraksta_sist=C4=93ma=2C_Atg=C4=81din=C4=81jums?=':
          M.store(num, '+FLAGS', '\\Deleted')

      print msg['Subject']

      date_tuple = email.utils.parsedate_tz(msg['Date'])
      if date_tuple:
          local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
      if local_date < last_date: # if this mail is older than the last checked --> stop
          break

#  print 'END'
  M.expunge()

# Function that lists available mailboxes
def listmailbox():
  try:
    print "Mailboxes:"
    for box in mailboxes:
      print box
  except:
    pass

# ============================================================================================

M = imaplib.IMAP4_SSL('imap.gmail.com')

try:
    M.login('info@vfabrika.lv', 'fabrika2017')
#    print "LOGED IN..."
except imaplib.IMAP4.error:
    print "LOGIN FAILED!!! "
    # ... exit or deal with failure...

rv, mailboxes = M.list()

#listmailbox()

#rv, data = M.select( mailboxes[0].split()[2] )
rv, data = M.select("[Gmail]/Sent Mail")
if rv == 'OK':
    process_mailbox(M)
    M.close()
M.logout()
