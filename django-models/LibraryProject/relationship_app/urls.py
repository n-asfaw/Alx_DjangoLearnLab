# relationship_app/urls.py

from django.urls import path
from . import views
from .views import list_books
from .views import LibraryDetailView
from .views import CustomLoginView, CustomLogoutView, RegisterView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # URL for the function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # URL for the class-based view
     path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

]





   