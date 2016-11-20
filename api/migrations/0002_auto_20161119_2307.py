# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('time', models.DateTimeField()),
                ('exerciseType', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('key', models.CharField(max_length=100)),
                ('exercise', models.ManyToManyField(to='api.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('word', models.CharField(max_length=100)),
                ('exercise', models.ManyToManyField(to='api.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Lowlight',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('key', models.CharField(max_length=100)),
                ('exercise', models.ManyToManyField(to='api.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('prompt', models.CharField(max_length=1000)),
                ('response', models.TextField()),
                ('needResponse', models.BooleanField(default=False)),
                ('exercise', models.ManyToManyField(to='api.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('time', models.DateTimeField()),
                ('score', models.IntegerField(default=-1)),
                ('faceID', models.IntegerField(default=-1)),
            ],
        ),
        migrations.RemoveField(
            model_name='dayentry',
            name='face',
        ),
        migrations.RemoveField(
            model_name='dayentry',
            name='rating',
        ),
        migrations.AddField(
            model_name='dayentry',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 19, 23, 7, 44, 611354, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='rating',
            name='dayEntry',
            field=models.ForeignKey(to='api.DayEntry'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='scoreAfter',
            field=models.OneToOneField(to='api.Rating'),
        ),
    ]
