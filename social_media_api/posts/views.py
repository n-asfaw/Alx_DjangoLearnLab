from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author__in=user.following.all()).order_by('-created_at')
