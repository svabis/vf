# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0009_auto_20170328_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klienti',
            name='tel',
            field=models.CharField(default=b'', max_length=16),
        ),
    ]
