# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0016_remove_planotajs_one'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grafiks',
            name='vietas',
            field=models.IntegerField(default=20),
        ),
    ]
