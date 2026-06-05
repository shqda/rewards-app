from rest_framework import serializers
from .models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "coins"]
        read_only_fields = ["coins"]

class RewardsLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardLog
        fields = ["amount", "given_at"]
