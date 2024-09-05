from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User, Score, Lobby, GameName, WordsLearned, Content

class UserTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123',
        }
        self.user = User.objects.create(**self.user_data)

    def test_create_user(self):
        response = self.client.post(reverse('create_user'), self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_get_users(self):
        response = self.client.get(reverse('get_users'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_user_detail(self):
        response = self.client.get(reverse('user_detail', kwargs={'pk': self.user.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)

    def test_update_user(self):
        update_data = {'username': 'updateduser'}
        response = self.client.put(reverse('user_detail', kwargs={'pk': self.user.id}), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')

    def test_delete_user(self):
        response = self.client.delete(reverse('user_detail', kwargs={'pk': self.user.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)


# class ScoreTests(TestCase):

#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create(username='player1', email='player1@example.com', password='password123')
#         self.score_data = {
#             'user': self.user.id,
#             'game_id': 1,
#             'score': 10,
#             'date': '2024-09-02T00:00:00Z'
#         }
#         self.score = Score.objects.create(user=self.user, game_id=1, score=10, date='2024-09-02T00:00:00Z')

#     def test_create_score(self):
#         response = self.client.post(reverse('create_score'), self.score_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Score.objects.count(), 2)

#     def test_get_scores(self):
#         response = self.client.get(reverse('get_scores'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)

#     def test_get_score_detail(self):
#         response = self.client.get(reverse('score_detail', kwargs={'pk': self.score.id}))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['score'], self.score.score)

#     def test_update_score(self):
#         update_data = {'score': 200}
#         response = self.client.put(reverse('score_detail', kwargs={'pk': self.score.id}), update_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.score.refresh_from_db()
#         self.assertEqual(self.score.score, 200)

#     def test_delete_score(self):
#         response = self.client.delete(reverse('score_detail', kwargs={'pk': self.score.id}))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Score.objects.count(), 0)


# class LobbyTests(TestCase):

#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create(username='lobbyowner', email='lobbyowner@example.com', password='password123')
#         self.lobby_data = {
#             'game_id': 1,
#             'owner_user': self.user.id,
#             'date': '2024-09-02T00:00:00Z',
#             'players': 4,
#             'game_type': 'Multiplayer'
#         }
#         self.game_name = GameName.objects.create(id=1, name='Multiplayer') 
#         self.lobby = Lobby.objects.create(game_id=1, owner_user=self.user, date='2024-09-02T00:00:00Z', players=4, game_type='Multiplayer')

#     def test_create_lobby(self):
#         response = self.client.post(reverse('create_lobby'), self.lobby_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Lobby.objects.count(), 2)

#     def test_get_lobbies(self):
#         response = self.client.get(reverse('get_lobbies'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)

#     def test_get_lobby_detail(self):
#         response = self.client.get(reverse('lobby_detail', kwargs={'pk': self.lobby.id}))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['game_type'], self.lobby.game_type)

#     def test_update_lobby(self):
#         update_data = {'players': 5}
#         response = self.client.put(reverse('lobby_detail', kwargs={'pk': self.lobby.id}), update_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.lobby.refresh_from_db()
#         self.assertEqual(self.lobby.players, 5)

#     def test_delete_lobby(self):
#         response = self.client.delete(reverse('lobby_detail', kwargs={'pk': self.lobby.id}))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Lobby.objects.count(), 0)


# Todo Change the name name!
# class GameNameTests(TestCase):

#     def setUp(self):
#         self.client = APIClient()
#         self.game_name_data = {'id': 1, 'name': 'Memo Game'}
#         self.game_name = GameName.objects.create(id=1, name='Memo Game') 

#     def test_create_game_name(self):
#         response = self.client.post(reverse('create_game_name'), self.game_name_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(GameName.objects.count(), 2)

#     def test_get_game_names(self):
#         response = self.client.get(reverse('get_game_names'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)

#     def test_get_game_name_detail(self):
#         response = self.client.get(reverse('game_name_detail', kwargs={'pk': self.game_name.id}))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['name'], self.game_name.name)

#     def test_delete_game_name(self):
#         response = self.client.delete(reverse('game_name_detail', kwargs={'pk': self.game_name.id}))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(GameName.objects.count(), 0)


# class WordsLearnedTests(TestCase):

#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create(username='learner', email='learner@example.com', password='password123')
#         self.content = Content.objects.create(content_id=1, japanese_slang='Konnichiwa', formal_version='Hello', description='A common greeting in Japanese.')
#         self.words_learned_data = {'user': self.user.id, 'content': self.content.id}
#         self.words_learned = WordsLearned.objects.create(user=self.user, content=self.content)

#     def test_create_words_learned(self):
#         response = self.client.post(reverse('create_words_learned'), self.words_learned_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(WordsLearned.objects.count(), 2)

#     def test_get_words_learned(self):
#         response = self.client.get(reverse('get_words_learned'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)

#     def test_get_words_learned_detail(self):
#         response = self.client.get(reverse('words_learned_detail', kwargs={'pk': self.words_learned.id}))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['user'], self.words_learned.user.id)

#     def test_update_words_learned(self):
#         new_content = Content.objects.create(content_id=2, japanese_slang='Ya-ho', formal_version='Hi', description='A common expression of XX in Japanese.')
#         update_data = {'content': new_content.id}


class QuickAnswerGameTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='learner', email='learner@example.com', password='password123')
        test_contents = [{"content_id":1, "japanese_slang":'Konnichiwa', 
                          "formal_version":'Hello', "description":'A common greeting in Japanese.'},
                         {"content_id":2, "japanese_slang":'Konnichiwa', 
                          "formal_version":'Hello', "description":'A common greeting in Japanese.'},
                         {"content_id":3, "japanese_slang":'Konnichiwa', 
                          "formal_version":'Hello', "description":'A common greeting in Japanese.'},
                         {"content_id":4, "japanese_slang":'Konnichiwa', 
                          "formal_version":'Hello', "description":'A common greeting in Japanese.'},
                         {"content_id":5, "japanese_slang":'Konnichiwa', 
                          "formal_version":'Hello', "description":'A common greeting in Japanese.'},
                         {"content_id":6, "japanese_slang":'Konnichiwa', 
                          "formal_version":'Hello', "description":'A common greeting in Japanese.'},
                         {"content_id":7, "japanese_slang":'Konnichiwa', 
                          "formal_version":'Hello', "description":'A common greeting in Japanese.'},
                         {"content_id":8, "japanese_slang":'Konnichiwa', 
                          "formal_version":'Hello', "description":'A common greeting in Japanese.'},
                         {"content_id":9, "japanese_slang":'Konnichiwa', 
                          "formal_version":'Hello', "description":'A common greeting in Japanese.'},
                         {"content_id":10, "japanese_slang":'Konnichiwa', 
                          "formal_version":'Hello', "description":'A common greeting in Japanese.'},]
        for i in test_contents:
            self.content = Content.objects.create(content_id=i.content_id, 
                                                  japanese_slang=i.japanese_slang, 
                                                  formal_version=i.formal_version, 
                                                  description=i.description)
        self.words_learned_data = {'user': self.user.id, 'content': self.content.content_id}
        self.words_learned = WordsLearned.objects.create(user=self.user, content=self.content)
        self.client = APIClient()

    # def test_get_random_problem(self):
    #     test_content = {
    #     "japanese_slang": "やばい",
    #     "formal_version": "危ない (あぶない)",
    #     "description": "This slang can mean something is dangerous or amazing depending on the context. This slang is heavily influenced by the context.",
    # }
    #     self.content = Content.objects.create(test_content)
    #     response1 = self.client.get(reverse('problem'), format='json')
    #     self.assertEqual(response1.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response1.data), 10)
    #     response2 = self.client.get(reverse('problem'), format='json')
    #     self.assertEqual(response2.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response2.data), 10)
    #     self.assertNotEqual(response1[0], response2[0])
    #     self.assertNotEqual(response1[10], response2[10])

    def test_quick_answer_game_content(self):
        response = self.client.get(reverse('deal'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # def test_get_words_learned_detail(self):
    #     response = self.client.get(reverse('words_learned_detail', kwargs={'pk': self.words_learned.id}))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['user'], self.words_learned.user.id)

    # def test_update_words_learned(self):
    #     new_content = Content.objects.create(content_id=2, japanese_slang='Ya-ho', formal_version='Hi', description='A common expression of XX in Japanese.')
    #     update_data = {'content': new_content.id}