# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pieraksts', '0005_auto_20170316_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atteikumi',
            name='nodarbiba',
            field=models.ForeignKey(related_name='ateikt', to='grafiks.Grafiks'),
        ),
    ]
