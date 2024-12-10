# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.PostListView.as_view(), name='post-list'),  # List view of all posts
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),  # Detail view of a single post
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),  # Edit an existing post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),  # Delete an existing post
     path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),  # Edit an existing post 
]
