# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodarb', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nodarb_tips',
            options={'verbose_name': 'Nodarbiba'},
        ),
        migrations.AlterModelOptions(
            name='tren_nodarb',
            options={'verbose_name': 'Relacija'},
        ),
        migrations.AlterModelOptions(
            name='treneris',
            options={'verbose_name': 'Treneri'},
        ),
    ]
