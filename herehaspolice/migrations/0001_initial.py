# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeoInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.FloatField(help_text='Please input Latitude', verbose_name='Latitude:')),
                ('lon', models.FloatField(help_text='Please input Longitude', verbose_name='Longitude:')),
                ('datetime_added', models.DateField(default=datetime.date.today)),
                ('text', models.CharField(help_text='Please Input Free Command', max_length=40, verbose_name='Free command:')),
            ],
        ),
    ]
