from django.db import models
from django.utils import timezone


# !!! Klienti !!!
class Klienti(models.Model):
    class Meta():
        verbose_name = 'Klienti'
        db_table = "klienti"

    pirmais_pieteikums = models.DateTimeField( default = timezone.now )
    pedejais_pieteikums = models.DateTimeField()
    vards = models.CharField( max_length = 50, default = '' )
    e_pasts = models.EmailField ()
    tel = models.IntegerField()
    pieteikuma_reizes = models.IntegerField()

    def __unicode__(self):
        return u'%s' % (self.vards)
