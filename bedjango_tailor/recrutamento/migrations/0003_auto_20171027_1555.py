# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-27 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recrutamento', '0002_auto_20171027_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga',
            name='descricao',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vaga',
            name='titulo',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
