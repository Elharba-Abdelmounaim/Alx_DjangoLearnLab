from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import CustomUser

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        
        all_users = CustomUser.objects.all()

        try:
            target_user = CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        request.user.following.add(target_user)
        return Response({'status': f'You are now following {target_user.username}'}, status=status.HTTP_200_OK)
