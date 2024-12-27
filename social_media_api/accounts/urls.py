from django.urls import path
from .views import UserFollowViewSet

urlpatterns = [
    path('follow/<int:user_id>/', UserFollowViewSet.as_view({'post': 'follow_user'}), name='follow-user'),
    path('unfollow/<int:user_id>/', UserFollowViewSet.as_view({'post': 'unfollow_user'}), name='unfollow-user'),
    # Add other URL patterns if needed
]
