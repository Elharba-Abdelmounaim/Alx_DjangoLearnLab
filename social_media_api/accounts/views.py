from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        request.user.following.add(target_user)
        return Response({'status': f'You are now following {target_user.username}'}, status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        request.user.following.remove(target_user)
        return Response({'status': f'You have unfollowed {target_user.username}'}, status=status.HTTP_200_OK)
