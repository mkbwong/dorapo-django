from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Card(models.Model):
    name_en = models.CharField(max_length=30, unique=True)
    name_ja = models.CharField(max_length=30, unique=True)
    hp = models.PositiveSmallIntegerField(default=0)
    attack = models.PositiveSmallIntegerField(default=0)
    defense = models.PositiveSmallIntegerField(default=0)
    level =  models.PositiveSmallIntegerField(default=0)
    ELEMENTS = (
                 ('Fire', 'Fire'),
                 ('Water', 'Water'),
                 ('Wood', 'Wood'),
               )
    element = models.CharField(max_length=5, choices=ELEMENTS)
    cost =  models.PositiveSmallIntegerField(default=0)
    orb =  models.PositiveSmallIntegerField(default=0)
    SKILL_TYPES = (
                    ('Fire', 'Fire'),
                    ('Water', 'Water'),
                    ('Wood', 'Wood'),
                    ('Hit','Hit'),
                    ('Slash','Slash'),
                  )
    skill_type = models.TextField(max_length=10, choices=SKILL_TYPES)
    skill_en = models.CharField(max_length=30)
    skill_desc_en = models.TextField() 
    #skill_properties = models.ManyToManyField(Properties)
    skill_ja = models.CharField(max_length=30)
    skill_desc_ja = models.TextField()
    subskill_en = models.CharField(max_length=30)
    subskill_desc_en = models.TextField()
    subskill_ja = models.CharField(max_length=30)
    subskill_desc_ja = models.TextField()
    #subskill_properties = models.ManyToMany(Properties)
    def __str__(self):
        return self.name_en


@python_2_unicode_compatible
class Property(models.Model):
    name = models.CharField(max_length=30, unique=True)
    desc = models.TextField()
    skill_relation = models.ManyToManyField(Card, related_name='skill_properties_set')
    subskill_relation = models.ManyToManyField(Card, related_name='subskill_properties_set')
    def __str__(self):
        return self.name
