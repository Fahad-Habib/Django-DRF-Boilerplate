"""Models of the users app."""

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.text import slugify


class CustomUserManager(BaseUserManager):
    """Custom User Manager."""

    def create_user(self, email, password=None, **extra_fields):
        """Create new user."""
        if not email:
            raise ValueError('Please enter an Email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, email, password=None, **extra_fields):
        """Create staff user."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self.create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create superuser."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """Custom User."""

    username = None
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

    handle = models.CharField(max_length=50, unique=True)
    picture = models.ImageField(upload_to='profile/', null=True, blank=True)
    about = models.TextField(max_length=200, blank=True)
    address = models.CharField(max_length=100, blank=True)
    contact = models.CharField(max_length=20, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        """Generate a handle while creating the user."""
        if not self.handle:
            self.handle = slugify(self.email)
        return super().save(*args, **kwargs)

    def __str__(self):
        """Return email of the user."""
        return self.email
