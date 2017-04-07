# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0007_auto_20170407_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grafiks',
            name='nodarbiba',
            field=models.ForeignKey(to='nodarb.Nodarb_tips'),
        ),
    ]
