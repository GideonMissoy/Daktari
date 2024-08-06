from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from .managers import UserManager


class User(AbstractUser):
    first_name = models.CharField(max_length=75, verbose_name=('First name'))
    last_name = models.CharField(max_length=75, verbose_name=('Last name'))
    email = models.EmailField(max_length=255, unique=True, verbose_name=_('Email Address'))
    phone_number = models.CharField(max_length=10)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def tokens(self):
        refresh=RefreshToken.for_user(self)
        return {
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }


class OneTimePassword(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    code=models.CharField(max_length=6, unique=True)

    def __str__(self):
        return f"(self.user.first_name)-passcode"


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    address = models.TextField()
    date_of_birth = models.DateField()


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')
    specialty = models.CharField(max_length=100)
    bio = models.TextField()
    consultation_fee = models.DecimalField(max_digits=6, decimal_places=2)
    is_verified = models.BooleanField(default=False)
