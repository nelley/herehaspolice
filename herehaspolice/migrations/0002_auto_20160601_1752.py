# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('herehaspolice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoinfo',
            name='datetime_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
