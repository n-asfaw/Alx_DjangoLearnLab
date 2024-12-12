# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('post/', view.PostListView.as_view(), name='post-list'),  # List view of all posts
    path('post/<int:pk>/', view.PostDetailView.as_view(), name='post-detail'),  # Detail view of a single post
    path('post/new/', view.PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('post/<int:pk>/update/', view.PostUpdateView.as_view(), name='post-update'),  # Edit an existing post
    path('post/<int:pk>/delete/', view.PostDeleteView.as_view(), name='post-delete'),  # Delete an existing post
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),  # View a post and its comments
    path('posts/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),  # Create a comment
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment-edit'),  # Edit a comment
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),  # Delete a comment
   
]
