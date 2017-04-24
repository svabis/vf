from django.db import models
from django.utils import timezone

#from klienti.models import Klienti
from grafiks.models import Grafiks


# !!! Klienti !!!
class Klienti(models.Model):
    class Meta():
        db_table = "klienti"

    pirmais_pieteikums = models.DateTimeField( default = timezone.now )
    pedejais_pieteikums = models.DateTimeField( default = timezone.now )
    vards = models.CharField( max_length = 50, default = '' )
    e_pasts = models.EmailField ()
    tel = models.CharField( max_length=16, default='' )
    pieteikuma_reizes = models.IntegerField( default=1 )
    atteikuma_reizes = models.IntegerField( default=0 )

    def __unicode__(self):
        return u'%s' % (self.vards)



# !!! Pieraksti !!!
class HistPieraksti(models.Model):
    class Meta():
        db_table = "hist_pieraksti"

    pieraksta_laiks = models.DateTimeField( default = timezone.now )
    klients = models.ForeignKey( Klienti )
    nodarbiba = models.ForeignKey( Grafiks )


# !!! Atteikumi !!!
class HistAtteikumi(models.Model):
    class Meta():
        db_table = "hist_atteikumi"

    ateikuma_laiks = models.DateTimeField( default = timezone.now )
    pieraksta_laiks = models.DateTimeField( default = timezone.now )
    klients = models.ForeignKey( Klienti )
    nodarbiba = models.ForeignKey( Grafiks )

