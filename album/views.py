from django.shortcuts import render
from album.models import Card

# Create your views here.
def card(request, name_en_slug):
    context_dict = {'name_en_slug': name_en_slug}

    try:
        card = Card.objects.get(name_en_slug=name_en_slug)
        context_dict['name_en'] = card.name_en
        context_dict['hp'] = card.hp
    except Card.DoesNotExist:
        pass

    return render(request, 'album/card.html', context_dict)

def index(request):
    context_dict = {'cards':Card.objects.all()}
    return render(request, 'album/index.html', context_dict)
