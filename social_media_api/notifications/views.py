from .models import Notification
from rest_framework import generics, permissions
from .serializers import NotificationSerializer

def create_notification(recipient, actor, verb, target):
    Notification.objects.create(
        recipient=recipient,
        actor=actor,
        verb=verb,
        target=target
    )

class NotificationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return self.request.user.notifications.all().order_by('-timestamp')
