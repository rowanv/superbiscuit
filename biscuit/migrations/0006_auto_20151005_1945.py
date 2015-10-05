# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('biscuit', '0005_auto_20151005_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='client_since',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 5, 19, 45, 38, 721077, tzinfo=utc)),
        ),
    ]
