from datetime import timedelta
from django.utils import timezone
from django.test import TestCase, override_settings

from .models import RewardLog, ScheduledReward, User
from rest_framework.test import APITestCase
from .views import REQUESTED_REWARD_AMOUNT


class UserModelTest(TestCase):
    def test_new_user_has_zero_coins(self):
        user = User.objects.create_user(username="Vasya", password="123")
        self.assertEqual(user.coins, 0)


class ProfileEndpointTest(APITestCase):
    def test_requires_auth(self):
        response = self.client.get("/api/profile/")
        self.assertEqual(response.status_code, 401)

    def test_returns_user_data(self):
        user = User.objects.create_user(username="Vasya")
        self.client.force_authenticate(user=user)
        response = self.client.get("/api/profile/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], "Vasya")

class RewardsEndpointTest(APITestCase):
    def test_requires_auth(self):
        response = self.client.get("/api/rewards/")
        self.assertEqual(response.status_code, 401)

    def test_empty_returns_no_data(self):
        user = User.objects.create_user(username="Vasya")
        self.client.force_authenticate(user=user)
        response = self.client.get("/api/rewards/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_returns_only_own_rewards(self):
        vasya = User.objects.create_user(username="Vasya")
        petya = User.objects.create_user(username="Petya")
        RewardLog.objects.create(user=vasya, amount=33)
        RewardLog.objects.create(user=petya, amount=44)
        self.client.force_authenticate(user=vasya)
        response = self.client.get("/api/rewards/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["amount"], 33)


        
        
