from rest_framework import permissions, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()

class UserFollowViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def follow_user(self, request, pk=None):
        user_to_follow = get_object_or_404(User, pk=pk)
        request.user.following.add(user_to_follow)
        return Response({'status': 'following'})

    def unfollow_user(self, request, pk=None):
        user_to_unfollow = get_object_or_404(User, pk=pk)
        request.user.following.remove(user_to_unfollow)
        return Response({'status': 'unfollowed'})

    def list_following(self, request):
        following = request.user.following.all()
        # Serialize the following users here if needed
        return Response({'following': [user.id for user in following]})
