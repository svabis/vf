from django.db import models
from django.utils import timezone

from klienti.models import Klienti
from grafiks.models import Grafiks

#import uuid

#def rand_code():
#    return str(uuid.uuid4())

# !!! Klienti !!!
class Pieraksti(models.Model):
    class Meta():
#        verbose_name = 'Pieraksti'
        db_table = "pieraksti"

    pieraksta_laiks = models.DateTimeField( default = timezone.now )
    klients = models.ForeignKey( Klienti )
    nodarbiba = models.ForeignKey( Grafiks )
#    atteikuma_kods = models.SlugField( unique = True, default=rand_code() )

#    def __unicode__(self):
#        return u'%s' % (self.nodarbiba)

