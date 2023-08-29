from django.contrib.auth.models import AbstractUser
from django.db import models

from m_a_s.models import NULLABLE


class User(AbstractUser):
    """User model for personality and permission abilities."""
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=40, verbose_name='phone', **NULLABLE)
    preview = models.ImageField(upload_to='users/', verbose_name='preview', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
