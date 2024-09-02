from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from uuid import uuid4



class CustomUserModelManager(BaseUserManager):
  def create_user(self, username, email, password=None):
    """
      Creates a custom user with the given fields
    """

    user = self.model(
      username = username,
      email = self.normalize_email(email),
    )

    user.set_password(password)
    user.save(using = self._db)

    return user

  
  def create_superuser(self, username, email, password):
    user = self.create_user(
      username,
      email,
      password = password
    )

    user.is_staff = True
    user.is_superuser = True
    user.save(using = self._db)

    return user


class CustomUserModel(AbstractBaseUser, PermissionsMixin):
  userId    = models.CharField(max_length = 64, default = uuid4, primary_key = True, editable = False)
  username  = models.CharField(max_length = 16, unique = True, null = False, blank = False)
  email     = models.EmailField(max_length = 100, unique = True, null = False, blank = False)

  USERNAME_FIELD = "username"
  REQUIRED_FIELDS = ["email"]

  active       = models.BooleanField(default = True)
  
  is_staff     = models.BooleanField(default = False)
  is_superuser = models.BooleanField(default = False)
  
  created_on   = models.DateTimeField(auto_now_add = True, blank = True, null = True)
  updated_at   = models.DateTimeField(auto_now = True)

  objects = CustomUserModelManager()

  class Meta:
    verbose_name = "Custom User"

# class User(AbstractUser):
#     phone_number = models.CharField(max_length=30)

#     def __str__(self):
#         return self.username

class Score(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    game_id = models.ForeignKey('lobby',to_field='game_id', on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.score}'

class Lobby(models.Model):
    game_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(CustomUserModel, related_name='lobby_owner', on_delete=models.CASCADE)
    players = models.ManyToManyField(CustomUserModel, related_name='joined_lobbies')
    game_type = models.ForeignKey('GameName', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Lobby for game {self.game_id} owned by {self.owner_user.username}'

class GameName(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class WordsLearned(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE)
    content = models.ForeignKey('Content', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} learned {self.content.japanese_slang}'

class Content(models.Model):
    content_id = models.AutoField(primary_key=True)
    japanese_slang = models.CharField(max_length=255)
    formal_version = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.japanese_slang
    


