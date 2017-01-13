# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0016_auto_20161215_0914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_id',
        ),
        migrations.AddField(
            model_name='student',
            name='mobile',
            field=models.CharField(default=1, max_length=11, verbose_name='\u624b\u673a'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='post_code',
            field=models.CharField(max_length=10, verbose_name='\u90ae\u7f16'),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.PositiveIntegerField(default=0, verbose_name='\u6027\u522b', choices=[(0, '\u5973'), (1, '\u7537')]),
        ),
    ]
