from rest_framework import serializers
from .models import User, Score, Lobby, GameName, WordsLearned, Content

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ScoreSerializer(serializers.ModelSerializer):
    player1 = serializers.CharField(source="player1.username")
    player2 = serializers.CharField(source="player2.username")
    class Meta:
        model = Score
        fields = ['id','score','date','player1', 'player2']

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

class WordsLearnedListSerializer(serializers.ModelSerializer):
    content = ContentSerializer()
    class Meta:
        model = WordsLearned
        fields = ['id', 'content']