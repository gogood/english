# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0015_order_orderdetail_shoppingcar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='order',
            field=models.OneToOneField(verbose_name='\u8ba2\u5355', to='index.Order'),
        ),
    ]
