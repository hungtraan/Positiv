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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateTimeField()),
                ('score', models.IntegerField(default=-1)),
                ('faceID', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('dayEntry', models.ForeignKey(to='api.DayEntry')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('exerciseType', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('key', models.CharField(max_length=100)),
                ('exercise', models.ManyToManyField(blank=True, to='api.ExerciseType')),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('word', models.CharField(max_length=100)),
                ('exercise', models.ManyToManyField(blank=True, to='api.ExerciseType')),
            ],
        ),
        migrations.CreateModel(
            name='Lowlight',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('key', models.CharField(max_length=100)),
                ('exercise', models.ManyToManyField(blank=True, to='api.ExerciseType')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('question_id', models.IntegerField(default=-1)),
                ('prompt', models.CharField(max_length=1000)),
                ('needResponse', models.BooleanField(default=False)),
                ('exercise', models.ForeignKey(null=True, to='api.ExerciseType')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('response', models.TextField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('exercise', models.ForeignKey(to='api.Exercise')),
                ('question', models.ForeignKey(to='api.Question')),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='exerciseType',
            field=models.ForeignKey(to='api.ExerciseType'),
        ),
    ]
