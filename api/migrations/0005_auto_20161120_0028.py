# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_exercise_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='dayEntry',
            field=models.ManyToManyField(null=True, to='api.DayEntry', blank=True),
        ),
        migrations.AlterField(
            model_name='highlight',
            name='exercise',
            field=models.ManyToManyField(null=True, to='api.Exercise', blank=True),
        ),
        migrations.AlterField(
            model_name='keyword',
            name='exercise',
            field=models.ManyToManyField(null=True, to='api.Exercise', blank=True),
        ),
        migrations.AlterField(
            model_name='lowlight',
            name='exercise',
            field=models.ManyToManyField(null=True, to='api.Exercise', blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='exercise',
            field=models.ManyToManyField(null=True, to='api.Exercise', blank=True),
        ),
    ]
