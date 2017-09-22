# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodarb', '0009_treneris_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodarb_tips',
            name='izcelt',
            field=models.BooleanField(default=False),
        ),
    ]
