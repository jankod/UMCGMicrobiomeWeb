from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models


class ProjectStatus(Enum):
    AC = "Active"
    NE = "Not active"


class CustomUser(AbstractUser):
    description = models.TextField(max_length=40_000)

    def __str__(self):
        return f"{self.username} {self.email}"


class Project(models.Model):
    name = models.CharField(max_length=240)
    description = models.TextField(max_length=40_000, blank=True)
    is_public = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in ProjectStatus])
    startDate = models.DateField(blank=True, null=True)
    project_admins = models.ManyToManyField(CustomUser)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
