# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20161119_2308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='dayEntry',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='scoreAfter',
        ),
        migrations.AddField(
            model_name='dayentry',
            name='faceID',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='dayentry',
            name='score',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='exercise',
            name='dayEntry',
            field=models.ManyToManyField(to='api.DayEntry'),
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
