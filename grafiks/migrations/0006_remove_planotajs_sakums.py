# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0005_auto_20170315_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planotajs',
            name='sakums',
        ),
    ]
