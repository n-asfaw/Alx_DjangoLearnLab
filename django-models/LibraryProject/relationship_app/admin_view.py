# views/admin_view.py

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .role_checks import is_admin  # Import the role check function

@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    return render(request, 'admin_view.html')
