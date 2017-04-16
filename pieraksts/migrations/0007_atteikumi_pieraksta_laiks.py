# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pieraksts', '0006_auto_20170316_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='atteikumi',
            name='pieraksta_laiks',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
