from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, FollowSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def follow(self, request, pk=None):
        target_user = self.get_object()
        request.user.following.add(target_user)
        return Response({'status': f'You are now following {target_user.username}'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def unfollow(self, request, pk=None):
        target_user = self.get_object()
        request.user.following.remove(target_user)
        return Response({'status': f'You have unfollowed {target_user.username}'}, status=status.HTTP_200_OK)
