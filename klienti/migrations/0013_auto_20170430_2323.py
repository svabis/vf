# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0012_histatteikumi_histpieraksti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='histatteikumi',
            name='nodarbiba',
            field=models.ForeignKey(related_name='hist_cancel', to='grafiks.Grafiks'),
        ),
        migrations.AlterField(
            model_name='histpieraksti',
            name='nodarbiba',
            field=models.ForeignKey(related_name='hist', to='grafiks.Grafiks'),
        ),
    ]
