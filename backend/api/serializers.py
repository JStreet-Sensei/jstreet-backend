from rest_framework import serializers
from .models import User, Score, Lobby, GameName, WordsLearned, Content

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

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
