from django.conf.urls import patterns, url
from album import views

urlpatterns = [ url(r'^$', views.index, name='index'),
                url(r'^(?P<name_en_slug>[\w-]+)/$', views.card, name='card'),
              ]
