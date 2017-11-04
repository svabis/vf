# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodarb', '0013_auto_20171104_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodarb_tips',
            name='slug',
            field=models.SlugField(default=b'auxtcxjc', unique=True),
        ),
        migrations.AlterField(
            model_name='treneris',
            name='slug',
            field=models.SlugField(default=b'toyerxst', unique=True),
        ),
    ]
