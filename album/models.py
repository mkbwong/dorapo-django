from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Card(models.Model):
    name_en = models.CharField(max_length=60, unique=True)
    translated_name_en = models.CharField(max_length=60, default='')
    name_ja = models.CharField(max_length=60, default='')
    hp = models.PositiveSmallIntegerField(default=0)
    attack = models.PositiveSmallIntegerField(default=0)
    defense = models.PositiveSmallIntegerField(default=0)
    level =  models.PositiveSmallIntegerField(default=0)
    EVO_CHOICES = (
                    ('N', 'N'),
                    ('N+','N+'),
                    ('R','R'),
                    ('R+','R+'),
                    ('S','S'),
                    ('S+','S+'),
                    ('SS','SS'),
                    ('SS+','SS+'),
                    ('GOD','GOD'),
                    ('DRA','DRA'),
                  )
    evo_base = models.CharField(max_length=3, choices=EVO_CHOICES, default='')
    evo_final = models.CharField(max_length=3, choices=EVO_CHOICES, default='')
    ELEMENTS = (
                 ('Fire', 'Fire'),
                 ('Water', 'Water'),
                 ('Wood', 'Wood'),
               )
    element = models.CharField(max_length=5, choices=ELEMENTS, default='')
    cost =  models.PositiveSmallIntegerField(default=0)
    orb =  models.PositiveSmallIntegerField(default=0)
    SKILL_TYPES = (
                    ('Fire', 'Fire'),
                    ('Water', 'Water'),
                    ('Wood', 'Wood'),
                    ('Hit','Hit'),
                    ('Slash','Slash'),
                  )
    main_skill_type = models.TextField(max_length=10, choices=SKILL_TYPES, default='')
    main_skill_en = models.CharField(max_length=60, default='')
    main_skill_desc_en = models.TextField(default='') 
    main_skill_ja = models.CharField(max_length=60, default='')
    main_skill_desc_ja = models.TextField(default='')
    subskill_en = models.CharField(max_length=60, default='')
    subskill_desc_en = models.TextField(default='')
    subskill_ja = models.CharField(max_length=60, default='')
    subskill_desc_ja = models.TextField(default='')
    # other relations used by this model:
    # Property - properties or tags of skills/subskills related using ManyToMany
    #            with separate intermediate tables for skill and subskill
    # Type - Card types like Girl, God, Eldritch, Demon, etc
    def __str__(self):
        return self.name_en

    name_en_slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        self.name_en_slug = slugify(self.name_en)
        super(Card, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Property(models.Model):
    name = models.CharField(max_length=30, unique=True)
    desc = models.TextField()
    skill_relation = models.ManyToManyField(Card, related_name='skill_properties_set')
    subskill_relation = models.ManyToManyField(Card, related_name='subskill_properties_set')
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Type(models.Model):
    type_en = models.CharField(max_length=30, unique=True)
    type_ja = models.CharField(max_length=30, default='')
    cardTypes = models.ManyToManyField(Card)
    def __str__(self):
        return self.name
