from django.test import TestCase

from .models import *;

class BasicTests(TestCase):
    def test_1(self):
        self.assertTrue(1==1)

    # def test_2(self):
    #     try:
    #         raise Exception("Failure test_2")
    #     except Exception as e:
    #         self.fail()

class TestModels(TestCase):
    def test_model_InventoryItem(self):
        self.user = User.objects.create(username="testuser", password ="password", email ="emailo@email.com")
    