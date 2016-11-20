# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20161119_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='time',
        ),
    ]
