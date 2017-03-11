# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0002_planotajs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planotajs',
            old_name='vieta',
            new_name='vietas',
        ),
    ]
