from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password_hash = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=15)


class Score(models.Model):
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    game_id = models.ForeignKey('lobby',to_field='game_id', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Lobby(models.Model):
    game_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, related_name='lobby_owner', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    players = models.ManyToManyField(User, related_name='joined_lobbies')
    game_type = models.ForeignKey('GameName', on_delete=models.CASCADE)


class GameName(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Content(models.Model):
    content_id = models.AutoField(primary_key=True)
    japanese_slang = models.CharField(max_length=255)
    formal_version = models.CharField(max_length=255)
    description = models.TextField()



class WordsLearned(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)

