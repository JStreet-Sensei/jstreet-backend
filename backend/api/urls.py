from django.urls import path
from .views import (
    GoogleLogin, get_users, create_user, user_detail,
    get_scores, create_score, score_detail,
    get_lobbies, create_lobby, lobby_detail,
    get_game_names, create_game_name, game_name_detail,
    get_words_learned, create_words_learned, words_learned_detail,
    get_content, create_content, content_detail,
    quick_answer_game_content
)

urlpatterns = [

    path("google/", GoogleLogin.as_view(), name="google_login"),

    # User URLs
    path('users/', get_users, name='get_users'),
    path('users/create', create_user, name='create_user'),
    path('users/<int:pk>/', user_detail, name='user_detail'),

    # Score URLs
    path('scores/', get_scores, name='get_scores'),
    path('scores/create', create_score, name='create_score'),
    path('scores/<int:pk>/', score_detail, name='score_detail'),

    # Lobby URLs
    path('lobbies/', get_lobbies, name='get_lobbies'),
    path('lobbies/create', create_lobby, name='create_lobby'),
    path('lobbies/<int:pk>/', lobby_detail, name='lobby_detail'),

    # GameName URLs
    path('game-names/', get_game_names, name='get_game_names'),
    path('game-names/create', create_game_name, name='create_game_name'),
    path('game-names/<int:pk>/', game_name_detail, name='game_name_detail'),

    # WordsLearned URLs
    path('words-learned/', get_words_learned, name='get_words_learned'),
    path('words-learned/create', create_words_learned, name='create_words_learned'),
    path('words-learned/<int:pk>/', words_learned_detail, name='words_learned_detail'),

    # Content URLs
    path('content/', get_content, name='get_content'),
    path('content/create', create_content, name='create_content'),
    path('content/<int:pk>/', content_detail, name='content_detail'),

    path('quick-answer-game/game-contents', quick_answer_game_content, name='quick_answer_game_content'),
]
