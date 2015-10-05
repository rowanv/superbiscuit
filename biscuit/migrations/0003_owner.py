# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biscuit', '0002_auto_20151005_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('owner_first_name', models.CharField(max_length=100)),
                ('owner_last_name', models.CharField(max_length=100)),
                ('owner_email', models.CharField(max_length=100)),
                ('owner_address_1', models.CharField(max_length=100, null=True, blank=True)),
                ('owner_address_2', models.CharField(max_length=100, null=True, blank=True)),
                ('owner_address_city', models.CharField(max_length=100, null=True, blank=True)),
                ('owner_address_state', models.CharField(max_length=100, null=True, blank=True)),
                ('owner_address_country', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
    ]
