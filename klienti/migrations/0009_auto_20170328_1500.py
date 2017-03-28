# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0008_auto_20170322_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klienti',
            name='tel',
            field=models.CharField(max_length=15),
        ),
    ]
