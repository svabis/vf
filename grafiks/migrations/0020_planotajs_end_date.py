# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0019_auto_20170703_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='planotajs',
            name='end_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
