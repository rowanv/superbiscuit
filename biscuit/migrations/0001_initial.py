# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('business_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('breed', models.CharField(default='Friendly Mutt', max_length=100)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Walker',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('walker_name', models.CharField(max_length=100)),
                ('business', models.ManyToManyField(blank=True, to='biscuit.Business')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='dog_walked',
            field=models.ForeignKey(to='biscuit.Dog'),
        ),
    ]
