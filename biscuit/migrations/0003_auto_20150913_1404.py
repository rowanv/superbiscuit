# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biscuit', '0002_auto_20150831_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100, default='Friendly Mutt')),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='dog_walked',
            field=models.ForeignKey(to='biscuit.Dog'),
        ),
    ]
