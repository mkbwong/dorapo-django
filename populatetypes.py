# -*- coding: utf-8 -*-


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dorapo.settings')

import django
django.setup()

from album.models import Card, SkillProperty, CardType

def main():
  types = {
            'None':               u'なし',            
            'Girl':               u'女の子',          
            'Robot':              u'ロボット',        
            'God':                u'神',              
            'Demon':              u'悪魔',            
            'Dragon':             u'ドラゴン',        
            'Battle Cat':         u'にゃんこ族',      
            'Million Arthur':     u'拡散族',          
            'Undead':             u'アンデット',      
            'Ninja':              u'忍者',            
            'Genie':              u'魔人',            
            'Eldritch':           u'邪神',            
            'Youkai':             u'妖怪',            
            'Angel':              u'天使',            
            'Merc Storia':        u'メルスト族',      
          }
  for typ in types:
    t = CardType.objects.get_or_create(type_en=typ,type_ja=types[typ])[0]
    t.save()


if __name__ == "__main__":
  main()

