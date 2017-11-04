# -*- coding: utf-8 -*-
from django.db import models

import random
import string

def rand_slug():
     add = ''.join(random.choice(string.ascii_letters) for _ in range(8))
     new_slug = add.lower()
     return new_slug


# !!! Nodarb_tips !!!
class Nodarb_tips(models.Model):
    class Meta():
        verbose_name = 'Nodarbiba'
        db_table = "nodarb_tips"

    nos = models.CharField( max_length = 100 )
    slug = models.SlugField( unique = True, default=rand_slug() )
    apraksts = models.TextField( default = 'apraksts' )
    redz = models.BooleanField( default = False )
    izcelt = models.BooleanField( default = False )

    def __unicode__(self):
        return u'%s' % (self.nos)

# !!! Treneris !!!
class Treneris(models.Model):
    class Meta():
        verbose_name = 'Treneri'
        db_table = "treneris"

    vards = models.CharField( max_length = 100 )
    slug = models.SlugField( unique = True, default=rand_slug() )
    apraksts = models.TextField( default = 'apraksts' )
    avatar = models.ImageField( blank = True, null=True, upload_to = "treneri/" )

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
    ('L', 'Lielā zāle'),
    ('M', 'Mazā zāle'),
    ('G', 'Gym zāle'),
    ('V', 'Velo zāle'),
    ('C', 'Cīņu zāle'),
)

# !!! Telpas !!!
class Telpa(models.Model):
    class Meta():
        verbose_name = 'Telpa'
        db_table = "telpa"

    telpa = models.CharField( max_length = 5, choices=TELPA_CHOISE )

    def __unicode__(self):
        return u'%s' % (self.telpa)

