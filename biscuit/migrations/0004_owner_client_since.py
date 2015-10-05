# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('biscuit', '0003_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='client_since',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 5, 19, 44, 42, 157011)),
        ),
    ]
