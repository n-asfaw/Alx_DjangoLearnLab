# advanced_features_and_security/managers.py

from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        """
        Create and return a regular user with a username and password.
        """
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, date_of_birth=date_of_birth, profile_photo=profile_photo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        """
        Create and return a superuser with the given username and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, date_of_birth, profile_photo, **extra_fields)
