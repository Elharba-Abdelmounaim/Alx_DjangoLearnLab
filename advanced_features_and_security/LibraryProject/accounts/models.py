from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.conf import settings


class CustomUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None, **extra_fields):
        if not email:
            raise ValueError('البريد الإلكتروني مطلوب')
        email = self.normalize_email(email)
        user = self.model(email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser يجب أن يكون is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser يجب أن يكون is_superuser=True')
        return self.create_user(email, date_of_birth, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True)

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['date_of_birth', 'username']  

    objects = CustomUserManager()

    def __str__(self):
        return self.email
