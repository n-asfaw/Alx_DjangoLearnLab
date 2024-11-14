# views/librarian_view.py

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .role_checks import is_librarian  # Import the role check function

@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    return render(request, 'librarian_view.html')
