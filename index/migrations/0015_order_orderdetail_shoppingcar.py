# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0014_auto_20161214_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.CharField(max_length=100, verbose_name='\u8ba2\u5355\u53f7')),
                ('favourable_money', models.IntegerField(verbose_name='\u4f18\u60e0\u91d1\u989d')),
                ('capital', models.IntegerField(verbose_name='\u5b9e\u4ed8\u91d1\u989d')),
                ('pay_time', models.DateTimeField(verbose_name='\u4ed8\u6b3e\u65f6\u95f4')),
                ('state', models.CharField(max_length=10, verbose_name='\u72b6\u6001')),
                ('bill', models.FileField(upload_to=b'static/doc', verbose_name='\u53d1\u7968')),
            ],
            options={
                'ordering': ['pay_time'],
                'verbose_name': '\u8ba2\u5355',
                'managed': True,
                'verbose_name_plural': '\u8ba2\u5355',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(verbose_name='\u6570\u91cf')),
                ('count_combo', models.ManyToManyField(to='index.CountCombo', verbose_name='\u6b21\u5361\u5957\u9910')),
                ('coupon', models.ManyToManyField(to='index.ReceiveCoupon', verbose_name='\u9886\u53d6\u4ee3\u91d1\u5238')),
                ('favourable_product', models.ManyToManyField(to='index.FavourableProduct', verbose_name='\u4f18\u60e0\u4ea7\u54c1')),
                ('month_combo', models.ManyToManyField(to='index.MonthCombo', verbose_name='\u5305\u6708\u5957\u9910')),
                ('order', models.ForeignKey(verbose_name='\u8ba2\u5355', to='index.Order')),
                ('pay_way', models.ForeignKey(verbose_name='\u4ed8\u6b3e\u65b9\u5f0f', to='index.PayWay')),
            ],
            options={
                'ordering': ['quantity'],
                'verbose_name': '\u8ba2\u5355\u8be6\u7ec6',
                'managed': True,
                'verbose_name_plural': '\u8ba2\u5355\u8be6\u7ec6',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count_combo', models.ManyToManyField(to='index.CountCombo', verbose_name='\u6b21\u5361\u5957\u9910')),
                ('month_combo', models.ManyToManyField(to='index.MonthCombo', verbose_name='\u5305\u6708\u5957\u9910')),
                ('student', models.OneToOneField(related_name='shopping_car_student', verbose_name='\u5b66\u5458', to='index.Student')),
            ],
            options={
                'ordering': ['student'],
                'verbose_name': '\u8d2d\u7269\u8f66',
                'managed': True,
                'verbose_name_plural': '\u8d2d\u7269\u8f66',
            },
        ),
    ]
