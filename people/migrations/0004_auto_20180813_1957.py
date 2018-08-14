# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20180515_1412'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': '\u5458\u5de5\u59d3\u540d', 'verbose_name_plural': '\u5458\u5de5\u4fe1\u606f'},
        ),
    ]
