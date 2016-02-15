# parses dorapowiki.xml dump from Special:Export page on wiki
# grabs all cards and their properties and commits them into django db
# invoke with 'python populatedbfromxml.py'
#   script must be in django project root
#   xml file must be in same directory
#   xml file had the page Template:Semantic Card Old manually deleted

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dorapo.settings')

import django
django.setup()

from album.models import Card, SkillProperty, CardType

import re
import xml.etree.ElementTree as ET

def main():
    cards = []
    root = ET.parse('dorapowiki.xml').getroot()
    ns = re.search(r'{.+}', root.tag).group()
    for page in root.findall(ns+'page'):
        dict = getBlankDict()
        dict['name_en']=page.find(ns+'title').text
        if dict['name_en'] == "Template:Semantic Card Old":
          next
        text = page.find(ns+'revision').find(ns+'text').text
        for key in dict.keys():
            try:
                dict[key]=re.search(key, text).group(1).strip()
            except AttributeError: #don't care if no match found on some attributes since wiki is not complete, default of blank is fine
                pass
        cards.append(dict)

    for x in cards:
        c = Card.objects.get_or_create(name_en=x['name_en'])[0]
        c.translated_name_en   =  x[r'Name\(en\)=(.*\n?)\|']
        c.name_ja =               x[r'Name\(ja\)=(.*\n?)\|']
        c.hp =                    x[r'HP=(.*\n?)\|']
        c.attack =                x[r'ATK=(.*\n?)\|']
        c.defense =               x[r'DEF=(.*\n?)\|']
        c.level =                 x[r'Level=(.*\n?)\|']
        c.evo_base =              x[r'Base Rarity=(.*\n?)\|']
        c.evo_final =             x[r'Max Rarity=(.*\n?)\|']
        c.element =               x[r'Element=(.*\n?)\|']
        c.cost =                  x[r'Cost=(.*\n?)\|']
        c.orb =                   x[r'Orb Socket=(.*\n?)\|']
        c.main_skill_type =       x[r'Skill Type=(.*\n?)\|']
        c.main_skill_en =         x[r'Main Skill\(en\)=(.*\n?)\|']
        c.main_skill_desc_en =    x[r'Main Skill Description\(en\)=(.*\n?)\|']
        c.main_skill_ja =         x[r'Main Skill\(ja\)=(.*\n?)\|']
        c.main_skill_desc_ja =    x[r'Main Skill Description\(ja\)=(.*\n?)\|']
        c.subskill_en =           x[r'Sub Skill\(en\)=(.*\n?)\|']
        c.subskill_desc_en =      x[r'Sub Skill Description\(en\)=(.*\n?)\|']
        c.subskill_ja =           x[r'Sub Skill\(ja\)=(.*\n?)\|']
        c.subskill_desc_ja =      x[r'Sub Skill Description\(ja\)=(.*\n?)\|']
        # extra logic for types because of many-to-many relation
        cardtypes = x[r'Types\(en\)=(.*\n?)\|'].strip().split(',')
        for x in cardtypes:
            if x == '':
                CardType.objects.get(type_en='None').card_set.add(c)
                continue

            CardType.objects.get(type_en=x.strip()).card_set.add(c)


        c.save()


def getBlankDict():
    dict = {
            r'Name\(en\)=(.*\n?)\|':'',
            r'Name\(ja\)=(.*\n?)\|':'',
            r'HP=(.*\n?)\|':0,
            r'ATK=(.*\n?)\|':0,
            r'DEF=(.*\n?)\|':0,
            r'Level=(.*\n?)\|':0,
            r'Base Rarity=(.*\n?)\|':'',
            r'Max Rarity=(.*\n?)\|':'',
            r'Element=(.*\n?)\|':'',
            r'Cost=(.*\n?)\|':0,
            r'Orb Socket=(.*\n?)\|':0,
            r'Skill Type=(.*\n?)\|':'',
            r'Main Skill\(en\)=(.*\n?)\|':'',
            r'Main Skill Description\(en\)=(.*\n?)\|':'',
            r'Main Skill\(ja\)=(.*\n?)\|':'',
            r'Main Skill Description\(ja\)=(.*\n?)\|':'',
            r'Sub Skill\(en\)=(.*\n?)\|':'',
            r'Sub Skill Description\(en\)=(.*\n?)\|':'',
            r'Sub Skill\(ja\)=(.*\n?)\|':'',
            r'Sub Skill Description\(ja\)=(.*\n?)\|':'',
            r'Types\(en\)=(.*\n?)\|':'', #store types as comma separated string for now, deal with it later when entering into db
            }
    return dict


if __name__=='__main__':
    main()
