from django.contrib import admin
from .models import User, Score, Lobby, GameName, WordsLearned, Content

admin.site.register(User)
admin.site.register(Score)
admin.site.register(Lobby)
admin.site.register(GameName)
admin.site.register(WordsLearned)
admin.site.register(Content)
