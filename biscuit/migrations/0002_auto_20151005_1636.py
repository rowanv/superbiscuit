# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biscuit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walker',
            name='business',
            field=models.ForeignKey(blank=True, null=True, to='biscuit.Business'),
        ),
    ]
