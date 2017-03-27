# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodarb', '0008_auto_20170322_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='treneris',
            name='avatar',
            field=models.ImageField(null=True, upload_to=b'treneri/', blank=True),
        ),
    ]
