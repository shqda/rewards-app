from django.test import TestCase

from .models import RewardLog, User
from rest_framework.test import APITestCase


class UserModelTest(TestCase):
    def test_new_user_has_zero_coins(self):
        user = User.objects.create_user(username="Vasya", password="123")
        self.assertEqual(user.coins, 0)


class ProfileEndpointTest(APITestCase):
    def test_profile_requires_auth(self):
        response = self.client.get("/api/profile/")
        self.assertEqual(response.status_code, 401)

    def test_profile_returns_user_data(self):
        user = User.objects.create_user(username="Vasya", password="123")
        self.client.force_authenticate(user=user)
        response = self.client.get("/api/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], "Vasya")
