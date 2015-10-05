# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biscuit', '0003_auto_20150913_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='walker',
            name='business',
        ),
    ]
