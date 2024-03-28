import uuid
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


# Create your models here.
class User(AbstractUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        USER = "USER", 'User'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    role = models.CharField(max_length=25, choices=Role.choices, default=Role.ADMIN)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=12, unique=True)
    first_name = models.CharField(max_length=255)
    otp = models.CharField(max_length=6)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['password']
    USERNAME_FIELD = 'phone_number'


class CustomUserManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Role.USER)


class CustomAdminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Role.ADMIN)


class CustomUser(User):
    objects = CustomUserManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.role = User.Role.USER
        return super().save(*args, **kwargs)


class CustomAdmin(User):
    objects = CustomAdminManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.role = User.Role.ADMIN
        return super().save(*args, **kwargs)
