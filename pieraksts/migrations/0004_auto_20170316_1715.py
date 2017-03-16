# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pieraksts', '0003_auto_20170316_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pieraksti',
            name='atteikuma_kods',
            field=models.SlugField(default=uuid.uuid4, unique=True),
        ),
    ]
