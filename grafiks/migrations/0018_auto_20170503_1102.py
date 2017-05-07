# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0017_auto_20170503_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grafiks',
            name='vietas',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='planotajs',
            name='vietas',
            field=models.IntegerField(default=20),
        ),
    ]
