# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20161120_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayentry',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
