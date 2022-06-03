from django.urls import path,include
from . import views

urlpatterns = [
    # room
    path('', views.signup_login, name='signup'),
    path('rooms/', views.index, name="rooms"),
    path('create_room/', views.create_room, name='create_room'),
    path('in_room/<int:room_id>/', views.in_room, name='in_room'),
    # path('rooms/', views.enter_room, name="enter_room"),
    # path('rooms/<room_name>', create_room, name="create_room"),

    # chat
    # path('send', views.send, name='send'),
    # path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    # path('getMessages/<int:room_id>/', views.getMessages, name='getMessages'),

]