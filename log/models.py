# -*- coding: utf-8 -*-
from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User


# !!!!! Log !!!!!
class Log(models.Model):
    class Meta():
        db_table = "log"

    log_user = models.ForeignKey( User )
    log_date = models.DateTimeField( default = timezone.now )
    log_event = models.CharField( max_length = 30 )

    log_event_data = models.CharField( max_length = 200 )

    def __unicode__(self):
        return u'%s' % (self.log_event)
