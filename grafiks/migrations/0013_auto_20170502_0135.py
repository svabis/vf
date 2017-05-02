# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0012_auto_20170502_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planotajs',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2017, 5, 2, 1, 35, 15, 934113)),
        ),
    ]
