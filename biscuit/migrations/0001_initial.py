# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('business_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Walker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('walker_name', models.CharField(max_length=100)),
                ('business_name', models.ForeignKey(to='biscuit.Business')),
            ],
        ),
    ]
