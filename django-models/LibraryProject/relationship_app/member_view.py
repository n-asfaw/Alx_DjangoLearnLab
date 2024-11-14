# views/member_view.py

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .role_checks import is_member  # Import the role check function

@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    return render(request, 'member_view.html')
