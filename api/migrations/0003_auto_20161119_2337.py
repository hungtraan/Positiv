# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20161119_2337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dayentry',
            old_name='d',
            new_name='date',
        ),
    ]
