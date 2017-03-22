# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodarb', '0007_nodarb_tips_rada'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nodarb_tips',
            old_name='rada',
            new_name='redz',
        ),
    ]
