from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import action

User = get_user_model()

class UserFollowViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def follow_user(self, request, pk=None):
        user_to_follow = get_object_or_404(User, pk=pk)
        request.user.following.add(user_to_follow)
        return Response({'status': 'following'})

    @action(detail=True, methods=['post'])
    def unfollow_user(self, request, pk=None):
        user_to_unfollow = get_object_or_404(User, pk=pk)
        request.user.following.remove(user_to_unfollow)
        return Response({'status': 'unfollowed'})
