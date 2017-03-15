# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planotajs',
            name='diena',
            field=models.IntegerField(default=0),
        ),
    ]
