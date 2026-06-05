from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
from .serializers import ProfileSerializer, RewardsLogSerializer
from .models import RewardLog


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)
