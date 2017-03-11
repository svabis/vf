from django.db import models
from nodarb.models import Nodarb_tips, Treneris, Telpa

# !!! Grafiks !!!
class Grafiks(models.Model):
    class Meta():
        db_table = "grafiks"

    sakums = models.DateTimeField()
#    ilgums = 
    nodarbiba = models.ForeignKey( Nodarb_tips ) # Nodarbiba
    treneris = models.ForeignKey( Treneris ) # Treneris
    telpa = models.ForeignKey( Telpa ) # Telpa
    vieta = models.IntegerField()

    def __unicode__(self):
        return self.nodarbiba.nos

# !!! Planotajs !!!
class Planotajs(models.Model):
    class Meta():
        db_table = "planotajs"

    sakums = models.DateTimeField()
#    ilgums =
    nodarbiba = models.ForeignKey( Nodarb_tips ) # Nodarbiba
    treneris = models.ForeignKey( Treneris ) # Treneris
    telpa = models.ForeignKey( Telpa ) # Telpa
    vietas = models.IntegerField()

    def __unicode__(self):
        return self.nodarbiba.nos
