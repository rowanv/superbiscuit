# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biscuit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Walker',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('walker_name', models.CharField(max_length=100)),
            ],
        ),
    ]
