from django.db import models
from django.contrib.auth.models import AbstractUser


class Client(AbstractUser):
    """
    Override default user model.
    """
    telegram_id = models.IntegerField(default=-1)
