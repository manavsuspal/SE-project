from django.urls import path 
from . import views 
from playground.models import *


urlpatterns = [
    path('login/', views.userlogin,name='login'),
    path('home/',views.home,name='home'),
    # path('event/',views.event_page),
    path('signup/',views.signup),
    path('search/', views.search_events,name='search'),
    # path('register/', views.register),
    path('logout/',views.userlogout)
]




for obj in Event.objects.all():
    urlpatterns.append(path(obj.slug, views.event_page))

