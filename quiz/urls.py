from django.urls import path,include

from quiz import views

urlpatterns = [
    path('', views.index)
]