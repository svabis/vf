# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0002_auto_20170314_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klienti',
            name='tel',
            field=models.CharField(max_length=8),
        ),
    ]
