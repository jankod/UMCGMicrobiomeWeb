from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models


class ProjectStatus(Enum):
    STARTED = "Started"
    ONGOING = "On going"
    ENDED = "Finished"


class CustomUser(AbstractUser):
    description = models.TextField(max_length=40_000)

    def __str__(self):
        return f"{self.username} {self.email}"


class Project(models.Model):
    NAME_LENGTH = 240

    name = models.CharField(max_length=NAME_LENGTH)
    DESCRIPTION_LENGTH = 40_000
    description = models.TextField(max_length=DESCRIPTION_LENGTH, blank=True)
    is_public = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in ProjectStatus])
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    user_admins = models.ManyToManyField(CustomUser, related_name='admins')
    user_participants = models.ManyToManyField(CustomUser, related_name='participants')
    user_creator = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
