# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0003_auto_20170315_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klienti',
            name='tel',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=8),
        ),
    ]
