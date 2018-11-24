from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    # add additional fields in here

    description = models.TextField()

    def __str__(self):
        return self.email
