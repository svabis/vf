# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0003_auto_20170311_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grafiks',
            old_name='vieta',
            new_name='vietas',
        ),
    ]
