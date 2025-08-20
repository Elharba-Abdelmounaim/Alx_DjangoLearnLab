from rest_framework import routers
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, feed

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', feed, name='feed'),
]
