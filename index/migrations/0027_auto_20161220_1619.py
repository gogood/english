# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0026_auto_20161219_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailcategory',
            name='main_category',
        ),
        migrations.RemoveField(
            model_name='detailcategory',
            name='small_category',
        ),
        migrations.RemoveField(
            model_name='detailcategory',
            name='sub_category',
        ),
        migrations.RemoveField(
            model_name='coursecategory',
            name='detail_category',
        ),
        migrations.AddField(
            model_name='coursecategory',
            name='small_category',
            field=models.ForeignKey(default=0, verbose_name='\u8be6\u7ec6\u5206\u7c7b', to='index.SmallCategory'),
        ),
        migrations.AddField(
            model_name='smallcategory',
            name='main_sub_category',
            field=models.ForeignKey(default=0, verbose_name='\u4e3b\u4e0e\u6b21\u5206\u7c7b', to='index.SubCategory'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='main_category',
            field=models.ForeignKey(default=0, verbose_name='\u4e3b\u5206\u7c7b\u540d', to='index.MainCategory'),
        ),
        migrations.DeleteModel(
            name='DetailCategory',
        ),
    ]
