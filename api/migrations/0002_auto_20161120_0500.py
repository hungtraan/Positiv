# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='exerciseType',
            field=models.ForeignKey(null=True, to='api.ExerciseType'),
        ),
    ]
