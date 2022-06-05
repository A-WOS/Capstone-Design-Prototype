from django.urls import path

import play.views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.play_round_after, name='success'),
    path('round/', views.play_round, name='round'),
]