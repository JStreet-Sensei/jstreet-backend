from django.contrib import admin

from .models import CustomUserModel,Score, Lobby, GameName, Content, WordsLearned

admin.site.register(CustomUserModel)
admin.site.register(Score)
admin.site.register(Lobby)
admin.site.register(GameName)
admin.site.register(Content)
admin.site.register(WordsLearned)
