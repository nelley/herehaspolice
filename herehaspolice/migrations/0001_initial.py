# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reportDT', models.DateTimeField(default=django.utils.timezone.now)),
                ('errorContent', models.CharField(help_text='Error Report', max_length=40, verbose_name='Error Report:')),
                ('ipaddress', models.GenericIPAddressField(help_text='IP Address', verbose_name='IP Address:')),
            ],
        ),
        migrations.CreateModel(
            name='GeoInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.FloatField(help_text='Please input Latitude', verbose_name='Latitude:')),
                ('lon', models.FloatField(help_text='Please input Longitude', verbose_name='Longitude:')),
                ('datetime_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.CharField(help_text='Please Input Free Command', max_length=40, verbose_name='Free command:')),
                ('ipaddress', models.GenericIPAddressField(help_text='IP Address', verbose_name='IP Address:')),
            ],
        ),
    ]
