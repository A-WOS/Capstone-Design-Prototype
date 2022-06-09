from django.contrib import admin
from .models import QuizRoom, QuizPlayers, Message


class QuizRoomAdmin(admin.ModelAdmin):
    search_fields = ['room_name']


class QuizPlayersAdmin(admin.ModelAdmin):
    search_fields = ['username']


class MessageAdmin(admin.ModelAdmin):
    search_fields = ['value']


admin.site.register(QuizRoom, QuizRoomAdmin)
admin.site.register(QuizPlayers, QuizPlayersAdmin)
admin.site.register(Message, MessageAdmin)
