# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DayEntry',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date', models.DateTimeField()),
                ('score', models.IntegerField(default=-1)),
                ('faceID', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('time', models.DateTimeField()),
                ('exerciseType', models.CharField(max_length=100)),
                ('dayEntry', models.ManyToManyField(to='api.DayEntry')),
            ],
        ),
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('key', models.CharField(max_length=100)),
                ('exercise', models.ManyToManyField(to='api.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('word', models.CharField(max_length=100)),
                ('exercise', models.ManyToManyField(to='api.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Lowlight',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('key', models.CharField(max_length=100)),
                ('exercise', models.ManyToManyField(to='api.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('prompt', models.CharField(max_length=1000)),
                ('response', models.TextField()),
                ('needResponse', models.BooleanField(default=False)),
                ('exercise', models.ManyToManyField(to='api.Exercise')),
            ],
        ),
    ]
