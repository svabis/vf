# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import grafiks.models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0002_planotajs_diena'),
    ]

    operations = [
        migrations.AddField(
            model_name='planotajs',
            name='laiks',
            field=models.TimeField(default=grafiks.models.default_start_time),
        ),
    ]
