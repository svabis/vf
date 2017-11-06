# -*- coding: utf-8 -*-
from django.db import models
from nodarb.models import Nodarb_tips, Treneris, Telpa
from datetime import datetime, timedelta

from django.utils import timezone

def default_start_time():
    now = datetime.now()
    start = now.replace(hour=8, minute=0, second=0, microsecond=0)
    return start

DAY_CHOISES = (
    ('0', 'Pirmdiena'),
    ('1', 'Otrdiena'),
    ('2', 'Trešdiena'),
    ('3', 'Ceturtdiena'),
    ('4', 'Piektdiena'),
    ('5', 'Sestdiena'),
    ('6', 'Svētdiena'),
)

# !!! Grafiks !!!
class Grafiks(models.Model):
    class Meta():
        db_table = "grafiks"

    sakums = models.DateTimeField()
    ilgums = models.IntegerField()
    nodarbiba = models.ForeignKey( Nodarb_tips, related_name='nd' ) # Nodarbiba
    treneris = models.ForeignKey( Treneris ) # Treneris
    telpa = models.ForeignKey( Telpa ) # Telpa
    vietas = models.IntegerField()

    def __unicode__(self):
        laiks = self.sakums + timedelta(hours=3)
        return laiks.strftime("%d/%m/%Y %H:%M") +' '+ self.nodarbiba.nos

# !!! Planotajs !!!
class Planotajs(models.Model):
    class Meta():
        db_table = "planotajs"

    diena = models.CharField( max_length = 15, default = 0, choices=DAY_CHOISES )
    laiks = models.TimeField( default=default_start_time )

    ilgums = models.IntegerField( default = 55 )
    nodarbiba = models.ForeignKey( Nodarb_tips ) # Nodarbiba
    treneris = models.ForeignKey( Treneris ) # Treneris
    telpa = models.ForeignKey( Telpa ) # Telpa
    vietas = models.IntegerField( default = 20 )

# for adding nodarbiba
    start_date = models.DateField( default = timezone.now )
    end_date = models.DateField( blank = True, null = True )

    def __unicode__(self):
        return self.nodarbiba.nos
