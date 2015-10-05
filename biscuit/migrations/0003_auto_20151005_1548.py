# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biscuit', '0002_auto_20151005_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='walker',
            name='business',
        ),
        migrations.AddField(
            model_name='walker',
            name='business',
            field=models.ForeignKey(default=None, to='biscuit.Business'),
            preserve_default=False,
        ),
    ]
