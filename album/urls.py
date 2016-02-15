from django.conf.urls import patterns, url
from album import views

urlpatterns = [ url(r'^$', views.index, name='index'),
                url(r'^search/', views.search, name='search'),
                url(r'^asearch/', views.asearch, name='asearch'),
                url(r'^autocomplete/', views.autocomplete, name='autocomplete'),
                url(r'^(?P<name_en_slug>[\w-]+)/$', views.card, name='card'),
              ]
