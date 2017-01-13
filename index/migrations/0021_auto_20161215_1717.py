# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0020_auto_20161215_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countcombo',
            name='italk_used',
            field=models.PositiveIntegerField(null=True, verbose_name='italk\u514d\u8d39\u4f7f\u7528\u6743\u6570', blank=True),
        ),
        migrations.AlterField(
            model_name='countcombo',
            name='italk_used_unit',
            field=models.CharField(default=b'\xe6\x9c\x88', max_length=10, verbose_name='italk\u514d\u8d39\u4f7f\u7528\u6743\u7684\u5355\u4f4d', blank=True),
        ),
        migrations.AlterField(
            model_name='countcombo',
            name='present_course',
            field=models.PositiveIntegerField(null=True, verbose_name='\u8d60\u9001\u8bfe\u7a0b\u6570', blank=True),
        ),
        migrations.AlterField(
            model_name='countcombo',
            name='present_course_unit',
            field=models.CharField(default=b'\xe8\x8a\x82', max_length=10, verbose_name='\u8d60\u9001\u8bfe\u7a0b\u6570\u7684\u5355\u4f4d', blank=True),
        ),
        migrations.AlterField(
            model_name='monthcombo',
            name='italk_used',
            field=models.PositiveIntegerField(null=True, verbose_name='italk\u514d\u8d39\u4f7f\u7528\u6743\u6570', blank=True),
        ),
        migrations.AlterField(
            model_name='monthcombo',
            name='italk_used_unit',
            field=models.CharField(default=b'\xe6\x9c\x88', max_length=10, verbose_name='italk\u514d\u8d39\u4f7f\u7528\u6743\u7684\u5355\u4f4d', blank=True),
        ),
        migrations.AlterField(
            model_name='monthcombo',
            name='present_course',
            field=models.PositiveIntegerField(null=True, verbose_name='\u8d60\u9001\u8bfe\u7a0b\u6570', blank=True),
        ),
        migrations.AlterField(
            model_name='monthcombo',
            name='present_course_unit',
            field=models.CharField(default=b'\xe8\x8a\x82', max_length=10, verbose_name='\u8d60\u9001\u8bfe\u7a0b\u6570\u7684\u5355\u4f4d', blank=True),
        ),
        migrations.AlterField(
            model_name='shoppingcar',
            name='count_combo',
            field=models.ManyToManyField(to='index.CountCombo', verbose_name='\u6b21\u5361\u5957\u9910', blank=True),
        ),
        migrations.AlterField(
            model_name='shoppingcar',
            name='month_combo',
            field=models.ManyToManyField(to='index.MonthCombo', verbose_name='\u5305\u6708\u5957\u9910', blank=True),
        ),
        migrations.AlterField(
            model_name='studentevaluate',
            name='content',
            field=models.CharField(max_length=1000, verbose_name='\u8bc4\u4ef7\u5185\u5bb9', blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='dynamic',
            field=models.CharField(max_length=1000, verbose_name='\u5916\u6559\u52a8\u6001', blank=True),
        ),
    ]
