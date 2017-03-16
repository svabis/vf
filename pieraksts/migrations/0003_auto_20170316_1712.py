# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieraksts', '0002_pieraksti_atteikuma_kods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pieraksti',
            name='atteikuma_kods',
            field=models.SlugField(default=b'8e0975ac-ba43-4922-b16e-3aeac6053922', unique=True),
        ),
    ]
