# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='evo_base',
            field=models.CharField(default=b'', max_length=3, choices=[(b'N', b'N'), (b'N+', b'N+'), (b'R', b'R'), (b'R+', b'R+'), (b'S', b'S'), (b'S+', b'S+'), (b'SS', b'SS'), (b'SS+', b'SS+'), (b'GOD', b'GOD'), (b'DRA', b'DRA')]),
        ),
        migrations.AddField(
            model_name='card',
            name='evo_final',
            field=models.CharField(default=b'', max_length=3, choices=[(b'N', b'N'), (b'N+', b'N+'), (b'R', b'R'), (b'R+', b'R+'), (b'S', b'S'), (b'S+', b'S+'), (b'SS', b'SS'), (b'SS+', b'SS+'), (b'GOD', b'GOD'), (b'DRA', b'DRA')]),
        ),
    ]
