from django.urls import path

import play.views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fail/', views.play_round_after_fail,),
    path('success/', views.play_round_after_success,),
]