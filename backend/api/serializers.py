from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import CustomUserModel, Score, Lobby, GameName, WordsLearned, Content
from .models import CustomUserModel
from django.conf import settings

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'

class LobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lobby
        fields = '__all__'

class GameNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameName
        fields = '__all__'

class WordsLearnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordsLearned
        fields = '__all__'

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

class CustomUserModelSerializer(ModelSerializer):
  class Meta:
    model = CustomUserModel
    fields = [
      "userId",
      "username",
      "email",
      "password",
    ]

  def create(self, validated_data):
    user = CustomUserModel.objects.create_user(
      validated_data["username"],
      validated_data["email"],
      validated_data["password"]
    )

    return user
