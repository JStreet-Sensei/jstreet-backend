from django.db import models
from django.contrib.auth.models import User

class Score(models.Model):
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    game_id = models.ForeignKey('lobby',to_field='game_id', on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.score}'

class Lobby(models.Model):
    game_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, related_name='lobby_owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='Lobby_default_name')
    game_type = models.ForeignKey('GameName', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Lobby for game {self.game_id} owned by {self.owner.username}'

class GameName(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class WordsLearned(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey('Content', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} learned {self.content.japanese_slang}'

class Content(models.Model):
    content_id = models.AutoField(primary_key=True)
    japanese_slang = models.CharField(max_length=255)
    english_slang = models.CharField(max_length=255)
    formal_version = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.japanese_slang
