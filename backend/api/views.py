from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Score, Lobby, GameName, WordsLearned, Content
from .serializers import (
    UserSerializer,
    ScoreSerializer,
    LobbySerializer,
    GameNameSerializer,
    WordsLearnedSerializer,
    ContentSerializer,
)
import random

from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client


# Google
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://127.0.0.1:3000/"
    client_class = OAuth2Client


# User views
@api_view(["GET"])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Score views
@api_view(["GET"])
def get_scores(request):
    scores = Score.objects.all()
    serializer = ScoreSerializer(scores, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_score(request):
    serializer = ScoreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def score_detail(request, pk):
    try:
        score = Score.objects.get(pk=pk)
    except Score.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ScoreSerializer(score)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ScoreSerializer(score, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        score.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Lobby views
@api_view(["GET"])
def get_lobbies(request):
    lobbies = Lobby.objects.all()
    serializer = LobbySerializer(lobbies, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_lobby(request):
    serializer = LobbySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def lobby_detail(request, pk):
    try:
        lobby = Lobby.objects.get(pk=pk)
    except Lobby.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = LobbySerializer(lobby)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = LobbySerializer(lobby, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        lobby.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# GameName views
@api_view(["GET"])
def get_game_names(request):
    game_names = GameName.objects.all()
    serializer = GameNameSerializer(game_names, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_game_name(request):
    serializer = GameNameSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def game_name_detail(request, pk):
    try:
        game_name = GameName.objects.get(pk=pk)
    except GameName.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = GameNameSerializer(game_name)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = GameNameSerializer(game_name, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        game_name.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# WordsLearned views
@api_view(["GET"])
def get_words_learned(request):
    words_learned = WordsLearned.objects.all()
    serializer = WordsLearnedSerializer(words_learned, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_words_learned(request):
    serializer = WordsLearnedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def words_learned_detail(request, pk):
    try:
        words_learned = WordsLearned.objects.get(pk=pk)
    except WordsLearned.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = WordsLearnedSerializer(words_learned)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = WordsLearnedSerializer(words_learned, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        words_learned.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Content views
@api_view(["GET"])
def get_content(request):
    content = Content.objects.all()
    serializer = ContentSerializer(content, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_content(request):
    serializer = ContentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def content_detail(request, pk):
    try:
        content = Content.objects.get(pk=pk)
    except Content.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ContentSerializer(content)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ContentSerializer(content, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        content.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
def quick_answer_game_content(request):
    """_summary_
    Get all data for a quick answer game. All problems, all deals for each users.
    Dictionary is like : {problems:[{content_id:..., japanese_slang}, ...],
    deals:[[slang1, slang2, slang2], [slang1, slang2, slang3], ...]}

    Args:
        request (_type_): Request should be get method.

    Returns:
        {
    "problems": [
        {
            "content_id": 4,
            "japanese_slang": "ぶっちゃけて言うと、... (ぶっちゃけていうと、...)",
            "english_slang": "To be honest,",
            "formal_version": "正直に言うと、... (しょうじきにいうと、...)",
            "description": "This slang is used to say 'to be honest' or 'to speak frankly.' It’s the same as the polite version."
        },....
        ,  "deals": [
        [
            {
                "content_id": 3,
                "japanese_slang": "ちょい待って！ (ちょいまって！)",
                "english_slang": "Wait!",
                "formal_version": "ちょっと待って。 (ちょっとまって。)",
                "description": "This slang means 'wait a bit' or 'hold on.' The polite way is '少々お待ちください。 (しょうしょうおまちください。)'"
            },...
        : Problems contains each problem user should solve. Deals has fake deals in every game.
    """
    if request.method == "GET":
        
        CONTENT_KEYS = list(
            Content.objects.values_list("content_id", flat=True).order_by("content_id")
        )
        content_keys_copied = CONTENT_KEYS.copy()
        problem_keys = []
        for i in range(10):
            problem_keys.append(random.choice(content_keys_copied))
            content_keys_copied.remove(problem_keys[len(problem_keys) - 1])
        problems = []
        for i in problem_keys:
            content = Content.objects.get(pk=i)
            problems.append(ContentSerializer(content).data)

        deals = []
        for i in problems:
            fake_range = CONTENT_KEYS
            fake_range.remove(i["content_id"])
            random.shuffle(fake_range)
            fakes_id = fake_range[:2]
            deal = []
            for k in fakes_id:
                content = Content.objects.get(pk=k)
                deal.append(ContentSerializer(content).data)
            deals.append(deal)
            return Response(
                data={"problems": problems, "deals": deals}, status=status.HTTP_200_OK
            )
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)