from datetime import timedelta
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
from .serializers import ProfileSerializer, RewardsLogSerializer
from .models import RewardLog, ScheduledReward
from .tasks import give_reward

REQUESTED_REWARD_AMOUNT = 10


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)


class RewardsLogView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = RewardsLogSerializer(
            RewardLog.objects.filter(user=request.user), many=True
        )
        return Response(serializer.data)


class ScheduledRewardView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        last = (
            ScheduledReward.objects.filter(user=request.user)
            .order_by("-execute_at")
            .first()
        )
        if last and last.execute_at >= timezone.now() - timedelta(days=1):
            ttw = last.execute_at + timedelta(days=1) - timezone.now()
            seconds = int(ttw.total_seconds())
            hours, mins, secs = seconds // 3600, (seconds % 3600) // 60, seconds % 60
            return Response(
                {
                    "info": f"reward available once a day, try again in {hours}h {mins}m {secs}s"
                },
                status=429,
            )
        reward = ScheduledReward.objects.create(
            user=request.user,
            amount=REQUESTED_REWARD_AMOUNT,
            execute_at=timezone.now() + timedelta(minutes=5),
        )
        give_reward.apply_async(args=[reward.id], eta=reward.execute_at)
        return Response({"status": "scheduled"}, status=201)
