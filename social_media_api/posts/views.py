from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

class UserFeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        following_users = request.user.following.all()  # Get the users that the current user follows
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  # Fetch posts from followed users
        # You can serialize and return the posts here
        post_data = [{'id': post.id, 'title': post.title, 'content': post.content, 'author': post.author.id} for post in posts]
        return Response(post_data)
