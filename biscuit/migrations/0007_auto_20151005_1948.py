# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('biscuit', '0006_auto_20151005_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='business',
            field=models.ForeignKey(null=True, to='biscuit.Business', blank=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='client_since',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 5, 19, 48, 36, 21645, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_email',
            field=models.EmailField(max_length=254),
        ),
    ]
