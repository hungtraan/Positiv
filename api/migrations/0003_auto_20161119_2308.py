# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20161119_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayentry',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
