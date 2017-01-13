# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0029_auto_20161222_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_apply_course',
            field=models.PositiveIntegerField(default=1, verbose_name='\u662f\u5426\u9884\u7ea6\u8bfe\u7a0b', choices=[(0, '\u662f'), (1, '\u5426')]),
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=b'11111111', max_length=20, verbose_name='\u767b\u5f55\u5bc6\u7801'),
        ),
        migrations.AddField(
            model_name='student',
            name='recomment_mobile',
            field=models.CharField(default=b'', max_length=11, verbose_name='\u63a8\u8350\u4eba\u7684\u624b\u673a\u53f7'),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=100, null=True, verbose_name='\u6536\u4ef6\u4eba\u7684\u5730\u5740', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(null=True, verbose_name='\u751f\u65e5', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='card_number',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='\u5269\u4f59\u6b21\u5361\u6570', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='english_name',
            field=models.CharField(default=b'Student', max_length=50, null=True, verbose_name='\u82f1\u6587\u540d\u5b57', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='lv',
            field=models.PositiveIntegerField(null=True, verbose_name='\u82f1\u8bed\u6c34\u5e73', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.CharField(max_length=11, verbose_name='\u624b\u673a'),
        ),
        migrations.AlterField(
            model_name='student',
            name='picture',
            field=models.ImageField(upload_to=b'static/images', null=True, verbose_name='\u5934\u50cf', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='post_code',
            field=models.CharField(max_length=10, null=True, verbose_name='\u90ae\u7f16', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='qq',
            field=models.CharField(max_length=20, null=True, verbose_name='QQ', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='recepient',
            field=models.CharField(max_length=50, null=True, verbose_name='\u6536\u4ef6\u4eba\u7684\u59d3\u540d', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='study_number',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='\u5b66\u8c46\u6570\u91cf', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='target',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='\u76ee\u6807\u7ea7\u522b', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='true_name',
            field=models.CharField(max_length=50, null=True, verbose_name='\u771f\u5b9e\u59d3\u540d', blank=True),
        ),
    ]
