# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_auto_20161214_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='coupon_id',
            field=models.CharField(max_length=10, verbose_name='\u4ee3\u91d1\u5238\u7684\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_date',
            field=models.DateField(verbose_name='\u6709\u6548\u671f'),
        ),
        migrations.AlterField(
            model_name='favourable',
            name='favourable_id',
            field=models.CharField(max_length=10, verbose_name='\u4f18\u60e0\u7f16\u53f7'),
        ),
    ]
