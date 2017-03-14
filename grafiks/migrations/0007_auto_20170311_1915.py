# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0006_auto_20170311_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grafiks',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
