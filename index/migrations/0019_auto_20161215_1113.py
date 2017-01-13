# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0018_auto_20161215_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receivecoupon',
            name='note',
        ),
        migrations.RemoveField(
            model_name='teachcourse',
            name='note',
        ),
        migrations.AlterField(
            model_name='book',
            name='money',
            field=models.PositiveIntegerField(verbose_name='\u91d1\u989d'),
        ),
        migrations.AlterField(
            model_name='countcombo',
            name='count_number',
            field=models.PositiveIntegerField(verbose_name='\u6b21\u5361\u6570\u91cf'),
        ),
        migrations.AlterField(
            model_name='countcombo',
            name='italk_used',
            field=models.PositiveIntegerField(verbose_name='italk\u514d\u8d39\u4f7f\u7528\u6743\u6570'),
        ),
        migrations.AlterField(
            model_name='countcombo',
            name='money',
            field=models.PositiveIntegerField(verbose_name='\u91d1\u989d'),
        ),
        migrations.AlterField(
            model_name='countcombo',
            name='present_course',
            field=models.PositiveIntegerField(verbose_name='\u8d60\u9001\u8bfe\u7a0b\u6570'),
        ),
        migrations.AlterField(
            model_name='countcombo',
            name='public_number',
            field=models.PositiveIntegerField(verbose_name='\u4f18\u9009\u516c\u5f00\u8bfe\u7684\u6570\u91cf'),
        ),
        migrations.AlterField(
            model_name='countcombo',
            name='unit',
            field=models.CharField(default=b'\xe8\xaf\xbe\xe6\x97\xb6', max_length=8, verbose_name='\u8bfe\u7684\u5355\u4f4d\uff0c\u9ed8\u8ba4\u4e3a\u8bfe\u65f6'),
        ),
        migrations.AlterField(
            model_name='countcombo',
            name='valid_date',
            field=models.PositiveIntegerField(verbose_name='\u6709\u6548\u671f'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='coupon_money',
            field=models.PositiveIntegerField(verbose_name='\u4ee3\u91d1\u5238\u7684\u91d1\u989d'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='state',
            field=models.PositiveIntegerField(default=0, verbose_name='\u4ee3\u91d1\u5238\u7684\u72b6\u6001', choices=[(0, '\u672a\u4f7f\u7528'), (1, '\u5df2\u4f7f\u7528'), (2, '\u5df2\u8fc7\u671f')]),
        ),
        migrations.AlterField(
            model_name='doctype',
            name='type_name',
            field=models.PositiveIntegerField(default=0, verbose_name='\u6587\u6863\u7c7b\u578b\u540d', choices=[(0, '\u590d\u4e60'), (1, '\u9884\u4e60')]),
        ),
        migrations.AlterField(
            model_name='favourable',
            name='favourable_money',
            field=models.PositiveIntegerField(verbose_name='\u4f18\u60e0\u91d1\u989d'),
        ),
        migrations.AlterField(
            model_name='favourableproduct',
            name='product_price',
            field=models.PositiveIntegerField(verbose_name='\u4f18\u60e0\u4ef7\u683c'),
        ),
        migrations.AlterField(
            model_name='monthcombo',
            name='italk_used',
            field=models.PositiveIntegerField(verbose_name='italk\u514d\u8d39\u4f7f\u7528\u6743\u6570'),
        ),
        migrations.AlterField(
            model_name='monthcombo',
            name='money',
            field=models.PositiveIntegerField(verbose_name='\u91d1\u989d'),
        ),
        migrations.AlterField(
            model_name='monthcombo',
            name='month_number',
            field=models.PositiveIntegerField(verbose_name='\u5305\u6708\u6570\u91cf'),
        ),
        migrations.AlterField(
            model_name='monthcombo',
            name='present_course',
            field=models.PositiveIntegerField(verbose_name='\u8d60\u9001\u8bfe\u7a0b\u6570'),
        ),
        migrations.AlterField(
            model_name='monthcombo',
            name='valid_date',
            field=models.PositiveIntegerField(verbose_name='\u6709\u6548\u671f'),
        ),
        migrations.AlterField(
            model_name='order',
            name='capital',
            field=models.PositiveIntegerField(verbose_name='\u5b9e\u4ed8\u91d1\u989d'),
        ),
        migrations.AlterField(
            model_name='order',
            name='favourable_money',
            field=models.PositiveIntegerField(verbose_name='\u4f18\u60e0\u91d1\u989d'),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.PositiveIntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u5df2\u4ed8\u6b3e'), (1, '\u672a\u4ed8\u6b3e')]),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='\u6570\u91cf'),
        ),
        migrations.AlterField(
            model_name='payway',
            name='pay_way_type',
            field=models.PositiveIntegerField(default=0, verbose_name='\u6536\u8d39\u65b9\u5f0f', choices=[(0, '12\u6708\u5206\u671f\u4ed8\u6b3e\uff0c\u6bcf\u6708\u7684\u91d1\u989d'), (1, '\u4e00\u6b21\u6027\u4ed8\u6e05')]),
        ),
        migrations.AlterField(
            model_name='setting',
            name='auto_substitute',
            field=models.PositiveIntegerField(default=0, verbose_name='\u7cfb\u7edf\u81ea\u52a8\u4ee3\u7406', choices=[(0, '\u542f\u52a8'), (0, '\u5173\u95ed')]),
        ),
        migrations.AlterField(
            model_name='setting',
            name='short_message',
            field=models.PositiveIntegerField(default=0, verbose_name='\u77ed\u4fe1\u63d0\u9192', choices=[(0, '\u63d0\u9192'), (1, '\u4e0d\u63d0\u9192')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.PositiveIntegerField(verbose_name='\u624b\u673a'),
        ),
        migrations.AlterField(
            model_name='studentevaluate',
            name='evaluate_type',
            field=models.PositiveIntegerField(default=0, verbose_name='\u8bc4\u4ef7\u7c7b\u578b', choices=[(0, '\u597d\u8bc4'), (1, '\u5dee\u8bc4')]),
        ),
        migrations.AlterField(
            model_name='studentevaluate',
            name='star_number',
            field=models.PositiveIntegerField(verbose_name='\u661f\u661f\u6570'),
        ),
        migrations.AlterField(
            model_name='studyrecord',
            name='state',
            field=models.PositiveIntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u5df2\u4e0a\u5b8c'), (1, '\u672a\u4e0a'), (2, '\u672a\u4e0a\u5b8c')]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='constellation',
            field=models.PositiveIntegerField(default=0, verbose_name='\u661f\u5ea7', choices=[(0, '\u767d\u7f8a\u5ea7'), (1, '\u91d1\u725b\u5ea7'), (2, '\u53cc\u5b50\u5ea7'), (3, '\u5de8\u87f9\u5ea7'), (4, '\u72ee\u5b50\u5ea7'), (5, '\u5904\u5973\u5ea7'), (6, '\u5929\u79e4\u5ea7'), (7, '\u5929\u874e\u5ea7'), (8, '\u5c04\u624b\u5ea7'), (9, '\u6469\u7faf\u5ea7'), (10, '\u6c34\u74f6\u5ea7'), (11, '\u53cc\u9c7c\u5ea7')]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='flowers_number',
            field=models.PositiveIntegerField(verbose_name='\u732e\u82b1\u6570'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='picture',
            field=models.ImageField(upload_to=b'static/images', verbose_name='\u5934\u50cf'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='shared_number',
            field=models.PositiveIntegerField(verbose_name='\u5206\u4eab\u6570'),
        ),
        migrations.AlterField(
            model_name='teacherevaluate',
            name='current_lv',
            field=models.PositiveIntegerField(default=0, verbose_name='\u5f53\u524d\u82f1\u8bed\u6c34\u5e73', choices=[(0, '\u96f6\u57fa\u7840'), (1, 'L1'), (2, 'L2'), (3, 'L3'), (4, 'L4'), (5, 'L5'), (6, 'L6'), (7, 'L7'), (8, 'L8'), (9, 'L9'), (10, 'L10'), (11, 'L11'), (12, 'L12')]),
        ),
        migrations.AlterField(
            model_name='teacherevaluate',
            name='fluency',
            field=models.PositiveIntegerField(default=0, verbose_name='\u6d41\u5229\u5ea6\u5206\u6570', choices=[(0, '1\u5206'), (1, '2\u5206'), (2, '3\u5206'), (3, '4\u5206'), (4, '5\u5206')]),
        ),
        migrations.AlterField(
            model_name='teacherevaluate',
            name='grammar',
            field=models.PositiveIntegerField(default=0, verbose_name='\u8bed\u6cd5\u5206\u6570', choices=[(0, '1\u5206'), (1, '2\u5206'), (2, '3\u5206'), (3, '4\u5206'), (4, '5\u5206')]),
        ),
        migrations.AlterField(
            model_name='teacherevaluate',
            name='listening',
            field=models.PositiveIntegerField(default=0, verbose_name='\u542c\u529b\u7406\u89e3\u5206\u6570', choices=[(0, '1\u5206'), (1, '2\u5206'), (2, '3\u5206'), (3, '4\u5206'), (4, '5\u5206')]),
        ),
        migrations.AlterField(
            model_name='teacherevaluate',
            name='pronunication',
            field=models.PositiveIntegerField(default=0, verbose_name='\u53d1\u97f3\u5206\u6570', choices=[(0, '1\u5206'), (1, '2\u5206'), (2, '3\u5206'), (3, '4\u5206'), (4, '5\u5206')]),
        ),
        migrations.AlterField(
            model_name='teacherevaluate',
            name='vocabulary',
            field=models.PositiveIntegerField(default=0, verbose_name='\u8bcd\u6c47\u5206\u6570', choices=[(0, '1\u5206'), (1, '2\u5206'), (2, '3\u5206'), (3, '4\u5206'), (4, '5\u5206')]),
        ),
    ]
