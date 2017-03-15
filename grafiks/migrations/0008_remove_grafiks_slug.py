# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0007_auto_20170311_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grafiks',
            name='slug',
        ),
    ]
