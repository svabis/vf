# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0015_auto_20170502_0206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planotajs',
            name='one',
        ),
    ]
