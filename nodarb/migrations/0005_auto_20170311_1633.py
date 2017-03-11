# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodarb', '0004_auto_20170311_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tren_nodarb',
            name='treneris',
            field=models.ForeignKey(related_name='t', to='nodarb.Treneris'),
        ),
    ]
