# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0025_auto_20161219_1113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detailcategory',
            options={'ordering': ['id'], 'managed': True, 'verbose_name': '\u8bfe\u7a0b\u8be6\u7ec6\u5206\u7c7b', 'verbose_name_plural': '\u8bfe\u7a0b\u8be6\u7ec6\u5206\u7c7b'},
        ),
        migrations.AlterModelOptions(
            name='maincategory',
            options={'ordering': ['id'], 'managed': True, 'verbose_name': '\u8bfe\u7a0b\u4e3b\u5206\u7c7b\u8868', 'verbose_name_plural': '\u8bfe\u7a0b\u4e3b\u5206\u7c7b\u8868'},
        ),
        migrations.AlterModelOptions(
            name='smallcategory',
            options={'ordering': ['id'], 'managed': True, 'verbose_name': '\u8bfe\u7a0b\u5c0f\u5206\u7c7b\u8868', 'verbose_name_plural': '\u8bfe\u7a0b\u5c0f\u5206\u7c7b\u8868'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ['id'], 'managed': True, 'verbose_name': '\u8bfe\u7a0b\u6b21\u5206\u7c7b\u8868', 'verbose_name_plural': '\u8bfe\u7a0b\u6b21\u5206\u7c7b\u8868'},
        ),
        migrations.AlterField(
            model_name='againstudyapply',
            name='study_record',
            field=models.OneToOneField(verbose_name='\u4e0a\u8bfe\u8bb0\u5f55', to='index.StudyRecord'),
        ),
        migrations.AlterField(
            model_name='book',
            name='course',
            field=models.ForeignKey(verbose_name='\u8bfe\u7a0b', to='index.Course'),
        ),
        migrations.AlterField(
            model_name='complain',
            name='study_record',
            field=models.ForeignKey(verbose_name='\u4e0a\u8bfe\u8bb0\u5f55', to='index.StudyRecord'),
        ),
        migrations.AlterField(
            model_name='countcombo',
            name='combo_type',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u7684\u7c7b\u578b', to='index.ComboType'),
        ),
        migrations.AlterField(
            model_name='coursecategory',
            name='course',
            field=models.ForeignKey(verbose_name='\u8bfe\u7a0b', to='index.Course'),
        ),
        migrations.AlterField(
            model_name='coursecategory',
            name='detail_category',
            field=models.ForeignKey(verbose_name='\u8be6\u7ec6\u5206\u7c7b', to='index.DetailCategory'),
        ),
        migrations.AlterField(
            model_name='detailcategory',
            name='main_category',
            field=models.ForeignKey(verbose_name='\u4e3b\u5206\u7c7b\u540d', to='index.MainCategory'),
        ),
        migrations.AlterField(
            model_name='detailcategory',
            name='small_category',
            field=models.ForeignKey(verbose_name='\u5c0f\u5206\u7c7b\u540d', to='index.SmallCategory'),
        ),
        migrations.AlterField(
            model_name='detailcategory',
            name='sub_category',
            field=models.ForeignKey(verbose_name='\u6b21\u5206\u7c7b\u540d', to='index.SubCategory'),
        ),
        migrations.AlterField(
            model_name='docsite',
            name='course',
            field=models.ForeignKey(verbose_name='\u8bfe\u7a0b', to='index.Course'),
        ),
        migrations.AlterField(
            model_name='monthcombo',
            name='combo_type',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u7684\u7c7b\u578b', to='index.ComboType'),
        ),
        migrations.AlterField(
            model_name='receivecoupon',
            name='coupon',
            field=models.ForeignKey(verbose_name='\u4ee3\u91d1\u5238', to='index.Coupon'),
        ),
        migrations.AlterField(
            model_name='receivecoupon',
            name='student',
            field=models.ForeignKey(verbose_name='\u5b66\u5458', to='index.Student'),
        ),
        migrations.AlterField(
            model_name='revisecourse',
            name='study_record',
            field=models.OneToOneField(verbose_name='\u4e0a\u8bfe\u8bb0\u5f55', to='index.StudyRecord'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='student',
            field=models.OneToOneField(default=b'', verbose_name='\u5b66\u751f', to='index.Student'),
        ),
        migrations.AlterField(
            model_name='shoppingcar',
            name='student',
            field=models.OneToOneField(verbose_name='\u5b66\u5458', to='index.Student'),
        ),
        migrations.AlterField(
            model_name='studentcollectteacher',
            name='student',
            field=models.ForeignKey(verbose_name='\u5b66\u751f', to='index.Student'),
        ),
        migrations.AlterField(
            model_name='studentcollectteacher',
            name='teacher',
            field=models.ForeignKey(verbose_name='\u5916\u6559', to='index.Teacher'),
        ),
        migrations.AlterField(
            model_name='studentevaluate',
            name='study_record',
            field=models.OneToOneField(verbose_name='\u4e0a\u8bfe\u8bb0\u5f55', to='index.StudyRecord'),
        ),
        migrations.AlterField(
            model_name='studentshareteacher',
            name='student',
            field=models.ForeignKey(verbose_name='\u5b66\u751f', to='index.Student'),
        ),
        migrations.AlterField(
            model_name='studentshareteacher',
            name='teacher',
            field=models.ForeignKey(verbose_name='\u5916\u6559', to='index.Teacher'),
        ),
        migrations.AlterField(
            model_name='studyrecord',
            name='course',
            field=models.ForeignKey(verbose_name='\u8bfe\u7a0b', to='index.Course'),
        ),
        migrations.AlterField(
            model_name='studyrecord',
            name='student',
            field=models.ForeignKey(verbose_name='\u5b66\u5458', to='index.Student'),
        ),
        migrations.AlterField(
            model_name='teachcourse',
            name='course',
            field=models.ForeignKey(verbose_name='\u8bfe\u7a0b', to='index.Course'),
        ),
        migrations.AlterField(
            model_name='teachcourse',
            name='teacher',
            field=models.ForeignKey(verbose_name='\u5916\u6559', to='index.Teacher'),
        ),
        migrations.AlterField(
            model_name='teacherevaluate',
            name='study_record',
            field=models.OneToOneField(verbose_name='\u4e0a\u8bfe\u8bb0\u5f55', to='index.StudyRecord'),
        ),
    ]
