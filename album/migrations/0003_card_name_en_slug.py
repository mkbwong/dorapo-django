# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_auto_20151230_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='name_en_slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
