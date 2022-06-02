from django.contrib import admin
from .models import QuizRoom, QuizPlayers


class QuizRoomAdmin(admin.ModelAdmin):
    search_fields = ['room_name']


class QuizPlayersAdmin(admin.ModelAdmin):
    search_fields = ['username']


admin.site.register(QuizRoom, QuizRoomAdmin)
admin.site.register(QuizPlayers, QuizPlayersAdmin)
