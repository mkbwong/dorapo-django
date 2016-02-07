from django.shortcuts import render
from album.models import Card
from django.db.models import Q

from .forms import BasicCardSearchForm
import md5

# Create your views here.
def card(request, name_en_slug):
    context_dict = {'name_en_slug': name_en_slug}

    try:
        card = Card.objects.get(name_en_slug=name_en_slug)
        context_dict['name_en'] =               card.name_en                   
        context_dict['translated_name_en'] =    card.translated_name_en        
        context_dict['name_ja'] =               card.name_ja                   
        context_dict['hp'] =                    card.hp                        
        context_dict['attack'] =                card.attack                    
        context_dict['defense'] =               card.defense                   
        context_dict['level'] =                 card.level                     
        context_dict['evo_base'] =              card.evo_base                  
        context_dict['evo_final'] =             card.evo_final                 
        context_dict['element'] =               card.element                   
        context_dict['cost'] =                  card.cost                      
        context_dict['orb'] =                   card.orb                       
        context_dict['main_skill_type'] =       card.main_skill_type           
        context_dict['main_skill_en'] =         card.main_skill_en             
        context_dict['main_skill_desc_en'] =    card.main_skill_desc_en        
        context_dict['main_skill_ja'] =         card.main_skill_ja             
        context_dict['main_skill_desc_ja'] =    card.main_skill_desc_ja        
        context_dict['subskill_en'] =           card.subskill_en               
        context_dict['subskill_desc_en'] =      card.subskill_desc_en          
        context_dict['subskill_ja'] =           card.subskill_ja               
        context_dict['subskill_desc_ja'] =      card.subskill_desc_ja          

        types = map(lambda t: t.type_en, card.type_set.all())
        context_dict['types'] =                 ', '.join(types)

        #get hashed directory name for card image
        m = md5.new(card.name_en.replace(' ','_')+'card.png')
        h = m.digest()[0].encode('hex')
        context_dict['cardimgurl'] = h[0]+r'/'+h+r'/'+card.name_en.replace(' ','_')+'card.png'
    except Card.DoesNotExist:
        pass

    return render(request, 'album/card.html', context_dict)

def index(request):
    context_dict = {'cards':Card.objects.all()}
    return render(request, 'album/index.html', context_dict)

def bsearch(request):
    try:
        name = request.GET['name']
        context_dict = {'results': Card.objects.filter(Q(name_en__icontains=name)|Q(name_ja__icontains=name))}
    except Card.DoesNotExist:
        context_dict = {'results':''}
    return render(request, 'album/bsearchresult.html', context_dict)

def get_card(request):
    form =  BasicCardSearchForm()
    return render(request, 'search.html', context_dict)

