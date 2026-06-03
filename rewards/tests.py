from django.test import TestCase
from .models import User


class UserModelTest(TestCase):
    def test_new_user_has_zero_coins(self):
        user = User.objects.create_user(username="Vasya", password="123")
        self.assertEqual(user.coins, 0)
