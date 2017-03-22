# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodarb', '0006_auto_20170311_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodarb_tips',
            name='rada',
            field=models.BooleanField(default=True),
        ),
    ]
