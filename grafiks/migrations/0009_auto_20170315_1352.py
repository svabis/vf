# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0008_remove_grafiks_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='grafiks',
            name='ilgums',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planotajs',
            name='ilgums',
            field=models.IntegerField(default=55),
        ),
    ]
