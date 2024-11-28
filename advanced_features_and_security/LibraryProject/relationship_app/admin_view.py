# admin_view.py

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

# Define the role check function for "Admin" role
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# Create the admin_view with access restriction
@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    # Optional: Custom forbidden response for non-admin logged-in users
    if not is_admin(request.user):
        return HttpResponseForbidden("You do not have permission to access this page.")
    # Render the admin view template if the user has the Admin role
    return render(request, 'admin_view.html')
