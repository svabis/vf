# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0006_remove_planotajs_sakums'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grafiks',
            name='nodarbiba',
            field=models.ForeignKey(related_name='nodarb_tips', to='nodarb.Nodarb_tips'),
        ),
    ]
