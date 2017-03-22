# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0006_auto_20170322_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='klienti',
            name='atteikuma_reizes',
            field=models.IntegerField(default=0),
        ),
    ]
