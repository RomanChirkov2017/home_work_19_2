from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')

    first_name = models.CharField(max_length=150, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=200, verbose_name='Фамилия', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='Страна', **NULLABLE)
    email_verified = models.BooleanField(default=False, verbose_name='Почта верифицирована')
    verification_token = models.CharField(max_length=100, blank=True, verbose_name='Код верификации')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []