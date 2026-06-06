from rest_framework import fields, serializers
from .models import ScheduledReward, User, RewardLog


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "coins"]
        read_only_fields = ["coins"]

class RewardsLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardLog
        fields = ["amount", "given_at"]
