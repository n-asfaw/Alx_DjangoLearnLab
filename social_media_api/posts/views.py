from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification



User = get_user_model()

class UserFeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        following_users = request.user.following.all()  # Get the users that the current user follows
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  # Fetch posts from followed users
        # You can serialize and return the posts here
        post_data = [{'id': post.id, 'title': post.title, 'content': post.content, 'author': post.author.id} for post in posts]
        return Response(post_data)



class LikeViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def like(self, request, pk):
        post = get_object_or_404(Post, pk=pk)  # This line retrieves the post
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if created:  # If the like was newly created
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )
            return Response({'status': 'liked'})
        return Response({'status': 'already liked'}, status=400)

    def unlike(self, request, pk):
        post = get_object_or_404(Post, pk=pk)  # This line retrieves the post
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({'status': 'unliked'})
        except Like.DoesNotExist:
            return Response({'status': 'not liked'}, status=400)