# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieraksts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pieraksti',
            name='atteikuma_kods',
            field=models.SlugField(default=b'2d48ce4d-46e8-4dd9-93b3-a163d23144cd'),
        ),
    ]
