# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biscuit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='walker',
            old_name='business_name',
            new_name='business',
        ),
    ]
