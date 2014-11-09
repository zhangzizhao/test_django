# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tt', '0002_auto_20141108_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='people',
            options={'ordering': ('city',)},
        ),
    ]
