# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campground',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('campground_code', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=256)),
                ('campground_type', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=256)),
                ('comments', models.TextField()),
                ('sites', models.CharField(max_length=256)),
                ('elevation', models.CharField(max_length=256)),
                ('hookups', models.CharField(max_length=256)),
                ('amenities', models.TextField()),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
