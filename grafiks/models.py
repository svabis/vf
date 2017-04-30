from django.db import models
from nodarb.models import Nodarb_tips, Treneris, Telpa
from datetime import datetime, timedelta

def default_start_time():
    now = datetime.now()
    start = now.replace(hour=8, minute=0, second=0, microsecond=0)
    return start

DAY_CHOISES = (
    ('0', 'P'),
    ('1', 'O'),
    ('2', 'T'),
    ('3', 'C'),
    ('4', 'Pk'),
    ('5', 'S'),
    ('6', 'Sv'),
)

# !!! Grafiks !!!
class Grafiks(models.Model):
    class Meta():
        db_table = "grafiks"
#        app_label = 'Grafiks'

    sakums = models.DateTimeField()
    ilgums = models.IntegerField()
    nodarbiba = models.ForeignKey( Nodarb_tips ) # Nodarbiba
    treneris = models.ForeignKey( Treneris ) # Treneris
    telpa = models.ForeignKey( Telpa ) # Telpa
    vietas = models.IntegerField()

    def __unicode__(self):
        laiks = self.sakums + timedelta(hours=3)
        return laiks.strftime("%d/%m/%Y %H:%M") +' '+ self.nodarbiba.nos
#        return self.nodarbiba.nos

# !!! Planotajs !!!
class Planotajs(models.Model):
    class Meta():
        db_table = "planotajs"
#        app_label = 'Planotajs'

#    sakums = models.DateTimeField()
    diena = models.CharField( max_length = 1, default = 0, choices=DAY_CHOISES )
    laiks = models.TimeField( default=default_start_time )

    ilgums = models.IntegerField( default = 55 )
    nodarbiba = models.ForeignKey( Nodarb_tips ) # Nodarbiba
    treneris = models.ForeignKey( Treneris ) # Treneris
    telpa = models.ForeignKey( Telpa ) # Telpa
    vietas = models.IntegerField()

    def __unicode__(self):
        return self.nodarbiba.nos
