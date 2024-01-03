from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
class CustomUserManager(BaseUserManager):
    def create_user(self, name, password=None, **extra_fields):
        if not name:
            raise ValueError('The Name field must be set')
        
        user = self.model(name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(name, password, **extra_fields)

class UserData(AbstractBaseUser):
    name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)  # Using CharField with length suitable for storing hashed passwords

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'name'

    def __str__(self):
        return self.name
