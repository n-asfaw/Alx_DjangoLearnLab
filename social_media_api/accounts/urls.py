from django.urls import path
from .views import UserFollowViewSet

urlpatterns = [
    path('follow/<int:pk>/', UserFollowViewSet.as_view({'post': 'follow_user'}), name='follow_user'),
    path('unfollow/<int:pk>/', UserFollowViewSet.as_view({'post': 'unfollow_user'}), name='unfollow_user'),
]
