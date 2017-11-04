# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodarb', '0011_auto_20171103_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treneris',
            name='slug',
            field=models.SlugField(default=b'yvkA', unique=True),
        ),
    ]
