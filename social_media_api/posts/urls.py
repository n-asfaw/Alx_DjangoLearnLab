from django.urls import path
from .views import UserFeedView

urlpatterns = [
    path('feed/', UserFeedView.as_view(), name='user_feed'),
    path('<int:pk>/like/', LikeViewSet.as_view({'post': 'like'}), name='like-post'),
    path('<int:pk>/unlike/', LikeViewSet.as_view({'post': 'unlike'}), name='unlike-post'),
]
