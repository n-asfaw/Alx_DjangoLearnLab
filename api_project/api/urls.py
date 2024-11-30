# api/urls.py

from django.urls import path
from .views import BookList


# Create a router and register the BookViewSet with it
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # URL for listing books
     path('', include(router.urls)),  # This includes all routes registered with the router

]
