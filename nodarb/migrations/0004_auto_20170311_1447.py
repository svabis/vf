# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodarb', '0003_telpa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodarb_tips',
            name='apraksts',
            field=models.TextField(default=b'apraksts'),
        ),
        migrations.AlterField(
            model_name='treneris',
            name='apraksts',
            field=models.TextField(default=b'apraksts'),
        ),
    ]
