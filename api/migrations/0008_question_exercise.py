# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20161120_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='exercise',
            field=models.ManyToManyField(blank=True, to='api.Exercise'),
        ),
    ]
