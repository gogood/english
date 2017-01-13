# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0027_auto_20161220_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit_name', models.CharField(max_length=20, verbose_name='\u5355\u4f4d\u540d')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u5355\u4f4d\u8868',
                'db_table': 't_unit',
                'managed': True,
                'verbose_name_plural': '\u5355\u4f4d\u8868',
            },
        ),
        migrations.RemoveField(
            model_name='course',
            name='setting',
        ),
        migrations.RemoveField(
            model_name='course',
            name='student_lv',
        ),
        migrations.AddField(
            model_name='course',
            name='course_number',
            field=models.PositiveIntegerField(default=0, verbose_name='\u8bfe\u7a0b\u6570'),
        ),
        migrations.AddField(
            model_name='course',
            name='pay_number',
            field=models.PositiveIntegerField(default=0, verbose_name='\u4ed8\u6b3e\u6570'),
        ),
        migrations.AddField(
            model_name='course',
            name='student_lv_height',
            field=models.PositiveIntegerField(default=0, verbose_name='\u9002\u5408\u5b66\u5458\u6c34\u5e732', choices=[(0, '\u96f6\u57fa\u7840'), (1, 'Lv1'), (2, 'Lv2'), (3, 'Lv3'), (4, 'Lv4'), (5, 'Lv5'), (6, 'Lv6'), (7, 'Lv7'), (8, 'Lv8'), (9, 'Lv9'), (10, 'Lv10'), (11, 'Lv11'), (12, 'Lv12'), (13, 'Lv13'), (14, 'Lv14'), (15, 'Lv15'), (16, 'Lv16')]),
        ),
        migrations.AddField(
            model_name='course',
            name='student_lv_low',
            field=models.PositiveIntegerField(default=0, verbose_name='\u9002\u5408\u5b66\u5458\u6c34\u5e731', choices=[(0, '\u96f6\u57fa\u7840'), (1, 'Lv1'), (2, 'Lv2'), (3, 'Lv3'), (4, 'Lv4'), (5, 'Lv5'), (6, 'Lv6'), (7, 'Lv7'), (8, 'Lv8'), (9, 'Lv9'), (10, 'Lv10'), (11, 'Lv11'), (12, 'Lv12'), (13, 'Lv13'), (14, 'Lv14'), (15, 'Lv15'), (16, 'Lv16')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=100, verbose_name='\u8bfe\u7a0b\u540d'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_unit',
            field=models.ForeignKey(related_name='course_course_unit', default=0, verbose_name='\u8bfe\u7a0b\u5355\u4f4d', blank=True, to='index.Unit'),
        ),
        migrations.AddField(
            model_name='course',
            name='pay_unit',
            field=models.ForeignKey(related_name='course_pay_unit', default=0, verbose_name='\u4ed8\u6b3e\u5355\u4f4d', blank=True, to='index.Unit'),
        ),
    ]
