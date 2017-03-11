# -*- coding: utf-8 -*-
from django.db import models

# !!! Nodarb_tips !!!
class Nodarb_tips(models.Model):
    class Meta():
        verbose_name = 'Nodarbiba'
        db_table = "nodarb_tips"

    nos = models.CharField( max_length = 100 )
    slug = models.SlugField( unique = True )
    apraksts = models.TextField( default = 'apraksts' )

    def __unicode__(self):
        return u'%s' % (self.nos)

# !!! Treneris !!!
class Treneris(models.Model):
    class Meta():
        verbose_name = 'Treneri'
        db_table = "treneris"

    vards = models.CharField( max_length = 100 )
    slug = models.SlugField( unique = True )
    apraksts = models.TextField( default = 'apraksts' )

    def __unicode__(self):
        return u'%s' % (self.vards)

# !!! Relacija !!!
class Tren_nodarb(models.Model):
    class Meta():
        verbose_name = 'Relacija'
        db_table = "tren_nodarb"

    nodarb = models.ForeignKey( Nodarb_tips, related_name='n' )
    treneris = models.ForeignKey( Treneris, related_name='t' )

    def __unicode__(self):
        return u'%s' % (self.nodarb)

TELPA_CHOISE = (
    ('L', 'lielā zāle'),
    ('M', 'mazā zāle'),
    ('G', 'gym zāle'),
    ('V', 'velo zāle'),
    ('C', 'cīņu zāle'),
)

# !!! Telpas !!!
class Telpa(models.Model):
    class Meta():
        verbose_name = 'Telpa'
        db_table = "telpa"

    telpa = models.CharField( max_length = 5, choices=TELPA_CHOISE )

    def __unicode__(self):
        return u'%s' % (self.telpa)

