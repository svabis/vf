# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodarb', '0005_auto_20170311_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tren_nodarb',
            name='nodarb',
            field=models.ForeignKey(related_name='n', to='nodarb.Nodarb_tips'),
        ),
    ]
