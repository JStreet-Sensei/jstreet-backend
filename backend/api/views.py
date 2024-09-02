from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Score, Lobby, GameName, WordsLearned, Content
from .serializers import UserSerializer, ScoreSerializer, LobbySerializer, GameNameSerializer, WordsLearnedSerializer, ContentSerializer

# User views
@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Score views
@api_view(['GET'])
def get_scores(request):
    scores = Score.objects.all()
    serializer = ScoreSerializer(scores, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_score(request):
    serializer = ScoreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def score_detail(request, pk):
    try:
        score = Score.objects.get(pk=pk)
    except Score.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ScoreSerializer(score)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ScoreSerializer(score, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        score.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Lobby views
@api_view(['GET'])
def get_lobbies(request):
    lobbies = Lobby.objects.all()
    serializer = LobbySerializer(lobbies, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_lobby(request):
    serializer = LobbySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def lobby_detail(request, pk):
    try:
        lobby = Lobby.objects.get(pk=pk)
    except Lobby.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LobbySerializer(lobby)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LobbySerializer(lobby, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        lobby.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# GameName views
@api_view(['GET'])
def get_game_names(request):
    game_names = GameName.objects.all()
    serializer = GameNameSerializer(game_names, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_game_name(request):
    serializer = GameNameSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def game_name_detail(request, pk):
    try:
        game_name = GameName.objects.get(pk=pk)
    except GameName.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GameNameSerializer(game_name)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GameNameSerializer(game_name, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        game_name.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# WordsLearned views
@api_view(['GET'])
def get_words_learned(request):
    words_learned = WordsLearned.objects.all()
    serializer = WordsLearnedSerializer(words_learned, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_words_learned(request):
    serializer = WordsLearnedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def words_learned_detail(request, pk):
    try:
        words_learned = WordsLearned.objects.get(pk=pk)
    except WordsLearned.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WordsLearnedSerializer(words_learned)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WordsLearnedSerializer(words_learned, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        words_learned.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Content views
@api_view(['GET'])
def get_content(request):
    content = Content.objects.all()
    serializer = ContentSerializer(content, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_content(request):
    serializer = ContentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def content_detail(request, pk):
    try:
        content = Content.objects.get(pk=pk)
    except Content.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContentSerializer(content)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContentSerializer(content, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        content.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
