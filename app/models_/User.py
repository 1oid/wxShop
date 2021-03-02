from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class UserModel(AbstractUser):
    phone = models.CharField(max_length=11, verbose_name="手机号")

    def __str__(self):
        return self.username
