from django.contrib import admin
from .models import Player, Quiz

class PlayerAdmin(admin.ModelAdmin):
    search_fields = ['player_name']

admin.site.register(Player,PlayerAdmin)

class QuizAdmin(admin.ModelAdmin):
    search_fields = ['quiz_title']

admin.site.register(Quiz,QuizAdmin)
# Register your models here.
