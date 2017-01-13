# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0028_auto_20161222_1109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['id'], 'managed': True, 'verbose_name': '\u8bfe\u7a0b\u8868', 'verbose_name_plural': '\u8bfe\u7a0b\u8868'},
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default=b'', upload_to=b'static/images', verbose_name='\u8bfe\u7a0b\u56fe\u7247'),
        ),
    ]
