# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0022_auto_20161217_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentevaluate',
            name='content',
        ),
        migrations.RemoveField(
            model_name='studentevaluate',
            name='evaluate_type',
        ),
        migrations.RemoveField(
            model_name='studentevaluate',
            name='star_number',
        ),
        migrations.AddField(
            model_name='studentevaluate',
            name='active_video',
            field=models.PositiveIntegerField(default=0, verbose_name='\u5916\u6559\u4e3b\u52a8\u89c6\u9891', choices=[(0, '\u662f'), (1, '\u5426')]),
        ),
        migrations.AddField(
            model_name='studentevaluate',
            name='attitute',
            field=models.PositiveIntegerField(default=0, verbose_name='\u6001\u5ea6\u597d\u8010\u5fc3\u5f15\u5bfc'),
        ),
        migrations.AddField(
            model_name='studentevaluate',
            name='book_content',
            field=models.TextField(verbose_name='\u5bf9\u6559\u6750\u7684\u8bc4\u8bed', blank=True),
        ),
        migrations.AddField(
            model_name='studentevaluate',
            name='book_difficult',
            field=models.PositiveIntegerField(default=0, verbose_name='\u6559\u6750\u7684\u96be\u5ea6', choices=[(0, '\u592a\u96be'), (1, '\u592a\u7b80\u5355'), (2, '\u9002\u4e2d')]),
        ),
        migrations.AddField(
            model_name='studentevaluate',
            name='book_interest',
            field=models.PositiveIntegerField(default=0, verbose_name='\u5bf9\u6559\u6750\u7684\u5174\u8da3', choices=[(0, '\u4e0d\u611f\u5174\u8da3'), (1, '\u4e00\u822c'), (2, '\u611f\u5174\u8da3')]),
        ),
        migrations.AddField(
            model_name='studentevaluate',
            name='book_quality',
            field=models.PositiveIntegerField(default=0, verbose_name='\u6559\u6750\u7684\u54c1\u8d28\uff08\u661f\u661f\u6570\uff09'),
        ),
        migrations.AddField(
            model_name='studentevaluate',
            name='broaden_knowledge',
            field=models.PositiveIntegerField(default=0, verbose_name='\u77e5\u8bc6\u62d3\u5c55\u4e0e\u7ea0\u9519\uff08\u661f\u661f\u6570\uff09'),
        ),
        migrations.AddField(
            model_name='studentevaluate',
            name='network',
            field=models.PositiveIntegerField(default=0, verbose_name='\u5916\u6559\u7f51\u7edc\u6548\u679c\uff08\u661f\u661f\u6570\uff09'),
        ),
        migrations.AddField(
            model_name='studentevaluate',
            name='on_time_class',
            field=models.PositiveIntegerField(default=0, verbose_name='\u5916\u6559\u6309\u65f6\u4e0a\u8bfe', choices=[(0, '\u662f'), (1, '\u5426')]),
        ),
        migrations.AddField(
            model_name='studentevaluate',
            name='pronunication_standard',
            field=models.PositiveIntegerField(default=0, verbose_name='\u5916\u6559\u53d1\u97f3\u6807\u51c6\uff08\u661f\u661f\u6570\uff09'),
        ),
        migrations.AddField(
            model_name='studentevaluate',
            name='tag',
            field=models.CharField(default=b'', max_length=1000, verbose_name='\u7ed9\u5916\u6559\u6253\u6807\u7b7e'),
        ),
        migrations.AddField(
            model_name='studentevaluate',
            name='teacher_content',
            field=models.TextField(verbose_name='\u5bf9\u5916\u6559\u7684\u8bc4\u8bed', blank=True),
        ),
    ]
