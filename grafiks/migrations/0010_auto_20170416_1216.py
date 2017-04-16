# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0009_auto_20170416_1215'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grafiks',
            options={'verbose_name': 'Grafik'},
        ),
        migrations.AlterModelOptions(
            name='planotajs',
            options={'verbose_name': 'Planotaj'},
        ),
    ]
