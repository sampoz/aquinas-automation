# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sensor_reading',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('sensor_name', models.CharField(max_length=100)),
                ('value', models.IntegerField()),
                ('created', models.DateTimeField(verbose_name='date recorded')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
