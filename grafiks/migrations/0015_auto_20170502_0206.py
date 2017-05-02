# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0014_auto_20170502_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planotajs',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
