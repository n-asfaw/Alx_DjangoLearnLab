from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.response import Response

User = get_user_model()

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        users = self.get_queryset()
        user_data = [{'id': user.id, 'email': user.email} for user in users]
        return Response(user_data)

class UserFollowView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user_to_follow = get_object_or_404(User, pk=pk)
        request.user.following.add(user_to_follow)
        return Response({'status': 'following'})

    def delete(self, request, pk):
        user_to_unfollow = get_object_or_404(User, pk=pk)
        request.user.following.remove(user_to_unfollow)
        return Response({'status': 'unfollowed'})
