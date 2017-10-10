from django.db import models

# !!!!! Dienas statistikas uzskaite !!!!!
class Logs(models.Model):
    class Meta():
        db_table = "log"

# datetime
# USER

# OBJECT
#   NAME/ID
#   COUNT

# action
#    ADD
#    DEL



#    x = models.IntegerField( default=0 )
#    y = models.IntegerField( default=0 )
#    def __unicode__(self):
#        return u'%s' % (self.x)

