# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=10, verbose_name=b'\xe8\xb4\xa6\xe6\x88\xb7')),
                ('password', models.CharField(max_length=10, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('email', models.EmailField(max_length=254, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
                ('phone', models.IntegerField(max_length=11, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81')),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(verbose_name=b'\xe5\xb9\xb4\xe9\xbe\x84'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=30, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d'),
        ),
    ]
