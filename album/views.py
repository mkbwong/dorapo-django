from django.http import HttpResponse
from django.shortcuts import render
from album.models import Card
from album.forms import CardForm
from django.db.models import Q
import json
import dorapotools as dt
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
        context_dict['main_skill_type_img'] =   '' if card.main_skill_type =='' else  dt.hashedDir(card.main_skill_type+'.png')
        context_dict['main_skill_type'] =       card.main_skill_type
        context_dict['main_skill_en'] =         card.main_skill_en             
        context_dict['main_skill_desc_en'] =    card.main_skill_desc_en        
        context_dict['main_skill_ja'] =         card.main_skill_ja             
        context_dict['main_skill_desc_ja'] =    card.main_skill_desc_ja        
        context_dict['subskill_en'] =           card.subskill_en               
        context_dict['subskill_desc_en'] =      card.subskill_desc_en          
        context_dict['subskill_ja'] =           card.subskill_ja               
        context_dict['subskill_desc_ja'] =      card.subskill_desc_ja          

        # converts the list of django models into their name attribute
        types = map(lambda t: u'{0} ({1})'.format(t.type_en, t.type_ja), card.types.all())
        context_dict['types'] =                 ', '.join(types)

        #get hashed directory name for card image
        context_dict['cardimgurl'] = dt.hashedDir(card.name_en.replace(' ','_')+'card.png')
    except Card.DoesNotExist:
        pass

    return render(request, 'album/card.html', context_dict)

def index(request):
    context_dict = {'cards':Card.objects.all()}
    return render(request, 'album/index.html', context_dict)

def search(request):
    try:
        name = request.GET['name']
        context_dict = {'results': Card.objects.filter(Q(name_en__icontains=name)|Q(name_ja__icontains=name))}
    except Card.DoesNotExist:
        context_dict = {'results':''}
    return render(request, 'album/searchresult.html', context_dict)

def asearch(request):
    form = CardForm()
    # just the asearch is requested, serve blank search form
    if request.get_full_path() == '/album/asearch/':
        return render(request, 'album/asearch.html', {'searchform': form})

    context_dict = {}
    q = Q()
    print request.GET['main_skill_type']
    for skill in request.GET.getlist('main_skill_type'):
        q.add(Q(main_skill_type__contains=skill), q.OR)

    context_dict['results']=Card.objects.filter(q)
    return render(request, 'album/searchresult.html', context_dict)

def autocomplete(request):
  cards = Card.objects.all()
  name=[{'name':c.name_en} for c in cards]
  name+=[{'name':c.name_ja} for c in cards]
  return HttpResponse(json.dumps(name))
