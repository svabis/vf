from django.db import models
from django.utils import timezone
#from phonenumber_field.modelfields import PhoneNumberField

# !!! Klienti !!!
class Klienti(models.Model):
    class Meta():
        verbose_name = 'Klienti'
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
