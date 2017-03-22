# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0007_klienti_atteikuma_reizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klienti',
            name='pieteikuma_reizes',
            field=models.IntegerField(default=1),
        ),
    ]
