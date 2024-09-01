from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.IntegerField()
    score = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username} - {self.score}'

class Lobby(models.Model):
    game_id = models.IntegerField()
    owner_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_lobbies')
    date = models.DateTimeField()
    players = models.IntegerField()
    game_type = models.TextField()

    def __str__(self):
        return f'Lobby for game {self.game_id} owned by {self.owner_user.username}'

class GameName(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

    def __str__(self):
        return self.name

class WordsLearned(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey('Content', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} learned {self.content.japanese_slang}'

class Content(models.Model):
    content_id = models.IntegerField(primary_key=True)
    japanese_slang = models.TextField()
    formal_version = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.japanese_slang
