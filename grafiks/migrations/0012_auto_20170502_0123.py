# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0011_auto_20170416_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='planotajs',
            name='one',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='planotajs',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 2, 1, 23, 52, 348760)),
        ),
    ]
