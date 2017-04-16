# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0008_auto_20170407_1158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grafiks',
            options={'verbose_name': 'Grafiks'},
        ),
        migrations.AlterModelOptions(
            name='planotajs',
            options={'verbose_name': 'Planotajs'},
        ),
    ]
