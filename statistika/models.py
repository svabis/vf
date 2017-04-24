from django.db import models

# !!!!! Dienas statistikas uzskaite !!!!!
class DayPierStat(models.Model):
    class Meta():
        db_table = "dienas_stat_dati"

    x = models.IntegerField( default=0 )
    y = models.IntegerField( default=0 )

    def __unicode__(self):
        return u'%s' % (self.x)

