# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0004_auto_20170311_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='grafiks',
            name='slug',
            field=models.SlugField(default=b'77ed3308-cd7f-44a3-8eaf-5b3636aa19a1', unique=True),
        ),
    ]
