# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20161120_0500'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighlightAnswer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('exercise', models.ForeignKey(to='api.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='LowlightAnswer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('exercise', models.ForeignKey(to='api.Exercise')),
            ],
        ),
        migrations.RemoveField(
            model_name='keyword',
            name='exercise',
        ),
        migrations.RemoveField(
            model_name='highlight',
            name='exercise',
        ),
        migrations.RemoveField(
            model_name='lowlight',
            name='exercise',
        ),
        migrations.AddField(
            model_name='dayentry',
            name='emotion',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='dayentry',
            name='sentiment',
            field=models.FloatField(default=0),
        ),
        migrations.DeleteModel(
            name='Keyword',
        ),
        migrations.AddField(
            model_name='lowlightanswer',
            name='loelight',
            field=models.ForeignKey(to='api.Lowlight', null=True),
        ),
        migrations.AddField(
            model_name='highlightanswer',
            name='highlight',
            field=models.ForeignKey(to='api.Highlight', null=True),
        ),
    ]
