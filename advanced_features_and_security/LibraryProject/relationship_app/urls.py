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
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),

]





   