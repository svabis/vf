# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0018_auto_20170503_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grafiks',
            name='nodarbiba',
            field=models.ForeignKey(related_name='nd', to='nodarb.Nodarb_tips'),
        ),
    ]
