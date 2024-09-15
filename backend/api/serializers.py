from rest_framework import serializers
from .models import User, Score, Lobby, GameName, WordsLearned, Content


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ScoreSerializer(serializers.ModelSerializer):
    winner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    loser = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    winner_username = serializers.SerializerMethodField()
    loser_username = serializers.SerializerMethodField()

    class Meta:
        model = Score
        fields = ["id", "score", "date", "winner", "loser", "winner_username", "loser_username"]

    def get_winner_username(self, obj):
        return obj.winner.username

    def get_loser_username(self, obj):
        return obj.loser.username

    def create(self, validated_data):
        winner = validated_data.pop("winner")
        loser = validated_data.pop("loser")
        score = validated_data.get("score")

        score_instance = Score.objects.create(winner=winner, loser=loser, score=score)
        return score_instance


class LobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lobby
        fields = "__all__"


class GameNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameName
        fields = "__all__"


class WordsLearnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordsLearned
        fields = "__all__"


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"


class WordsLearnedListSerializer(serializers.ModelSerializer):
    content = ContentSerializer()

    class Meta:
        model = WordsLearned
        fields = ["id", "content", "created_at"]
