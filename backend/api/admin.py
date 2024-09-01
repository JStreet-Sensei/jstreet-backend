from django.contrib import admin

from .models import User,Score, Lobby, GameName, Content, WordsLearned

admin.site.register(User)
admin.site.register(Score)
admin.site.register(Lobby)
admin.site.register(GameName)
admin.site.register(Content)
admin.site.register(WordsLearned)
