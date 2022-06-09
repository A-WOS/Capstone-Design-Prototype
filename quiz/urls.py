from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # room
    path('', views.signup_login, name='signup'),
    path('logout/', views.remove_account, name='logout'),
    path('rooms/', views.index, name="rooms"),
    path('create_room/', views.create_room, name='create_room'),
    path('in_room/<int:room_id>/', views.in_room, name='in_room'),

    path('send', views.send, name='send'),
    path('getMessages/<int:room_id>/', views.getMessages, name='getMessages'),
    # path('getMessages/', views.getMessages, name='getMessages'),
    # path('getMessages/<str:room>/', views.getMessages, name='getMessages'),

    # chat



]