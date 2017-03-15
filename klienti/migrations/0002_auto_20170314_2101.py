# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klienti',
            name='pedejais_pieteikums',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
