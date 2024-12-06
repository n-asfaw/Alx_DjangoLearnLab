from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This handles the base URL "/"
    # Other URL patterns
   
]
