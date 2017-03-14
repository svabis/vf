# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0005_grafiks_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grafiks',
            name='slug',
            field=models.SlugField(default=b'0084e84cfd57dfc5a2e6f6289d8d3f2a', unique=True),
        ),
    ]
