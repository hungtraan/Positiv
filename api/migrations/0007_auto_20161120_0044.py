# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20161120_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('response', models.TextField()),
                ('needResponse', models.BooleanField(default=False)),
                ('exercise', models.ManyToManyField(to='api.Exercise', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='exercise',
        ),
        migrations.RemoveField(
            model_name='question',
            name='needResponse',
        ),
        migrations.RemoveField(
            model_name='question',
            name='response',
        ),
        migrations.AddField(
            model_name='questionanswer',
            name='question',
            field=models.ForeignKey(to='api.Question'),
        ),
    ]
