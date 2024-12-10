# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),  # List view of all posts
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),  # Detail view of a single post
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),  # Edit an existing post
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),  # Delete an existing post
]
