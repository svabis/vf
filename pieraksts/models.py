from django.db import models
from django.utils import timezone

from klienti.models import Klienti
from grafiks.models import Grafiks

import uuid


# !!! Pieraksti !!!
class Pieraksti(models.Model):
    class Meta():
        verbose_name = 'Pieraksti'
        db_table = "pieraksti"

    pieraksta_laiks = models.DateTimeField( default = timezone.now )
    klients = models.ForeignKey( Klienti )
    nodarbiba = models.ForeignKey( Grafiks, related_name='nod'  )
    atteikuma_kods = models.SlugField( unique=True, default=uuid.uuid4 )


# !!! Atteikumi !!!
class Atteikumi(models.Model):
    class Meta():
        verbose_name = 'Atteikumi'
        db_table = "atteikumi"

    pieraksta_laiks = models.DateTimeField( default = timezone.now )
    ateikuma_laiks = models.DateTimeField( default = timezone.now )
    klients = models.ForeignKey( Klienti )
    nodarbiba = models.ForeignKey( Grafiks, related_name='ateikt' )

