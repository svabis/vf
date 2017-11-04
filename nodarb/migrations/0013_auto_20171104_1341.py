# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodarb', '0012_auto_20171104_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treneris',
            name='slug',
            field=models.SlugField(default=b'kiyt', unique=True),
        ),
    ]
