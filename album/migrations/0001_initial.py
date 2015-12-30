# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_en', models.CharField(unique=True, max_length=30)),
                ('name_ja', models.CharField(default=b'', max_length=30)),
                ('hp', models.PositiveSmallIntegerField(default=0)),
                ('attack', models.PositiveSmallIntegerField(default=0)),
                ('defense', models.PositiveSmallIntegerField(default=0)),
                ('level', models.PositiveSmallIntegerField(default=0)),
                ('element', models.CharField(default=b'', max_length=5, choices=[(b'Fire', b'Fire'), (b'Water', b'Water'), (b'Wood', b'Wood')])),
                ('cost', models.PositiveSmallIntegerField(default=0)),
                ('orb', models.PositiveSmallIntegerField(default=0)),
                ('skill_type', models.TextField(default=b'', max_length=10, choices=[(b'Fire', b'Fire'), (b'Water', b'Water'), (b'Wood', b'Wood'), (b'Hit', b'Hit'), (b'Slash', b'Slash')])),
                ('skill_en', models.CharField(default=b'', max_length=30)),
                ('skill_desc_en', models.TextField(default=b'')),
                ('skill_ja', models.CharField(default=b'', max_length=30)),
                ('skill_desc_ja', models.TextField(default=b'')),
                ('subskill_en', models.CharField(default=b'', max_length=30)),
                ('subskill_desc_en', models.TextField(default=b'')),
                ('subskill_ja', models.CharField(default=b'', max_length=30)),
                ('subskill_desc_ja', models.TextField(default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('desc', models.TextField()),
                ('skill_relation', models.ManyToManyField(related_name='skill_properties_set', to='album.Card')),
                ('subskill_relation', models.ManyToManyField(related_name='subskill_properties_set', to='album.Card')),
            ],
        ),
    ]
