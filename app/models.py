import os
from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ForeignKey
from django.urls import reverse

PREMISSION_ADMIN = "admin"


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
    DESCRIPTION_LENGTH = 40_000

    name = models.CharField(max_length=NAME_LENGTH)
    description = models.TextField(max_length=DESCRIPTION_LENGTH, blank=True)
    is_public = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=[(tag.name, tag.value) for tag in ProjectStatus])
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Rel
    user_admins = models.ManyToManyField(CustomUser, related_name='admins')
    user_participants = models.ManyToManyField(CustomUser, related_name='participants')
    user_creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.name}"

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('app_project_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('app_project_update', args=(self.pk,))


class Sample(models.Model):
    NAME_LENGTH = 240
    DESCRIPTION_LENGTH = 40_000

    name = models.CharField(max_length=NAME_LENGTH)
    description = models.TextField(max_length=DESCRIPTION_LENGTH, blank=True, null=True)

    year_birth = models.SmallIntegerField()
    is_male = models.BooleanField()
    bmi = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    # Relationship Fields
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="projects")

    class Meta:
        ordering = ('-created_at',)

    def __unicode__(self):
        return u'%s' % self.pk

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app_sample_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('app_sample_update', args=(self.pk,))


class SampleFiles(models.Model):
    # Fields
    file_name = models.CharField(max_length=240)
    file = models.FileField(upload_to="upload/files/")
    type = models.CharField(max_length=40)
    description = models.TextField(max_length=40_000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Relationship Fields
    sample = ForeignKey(Sample, on_delete=models.CASCADE, related_name="samples")

    class Meta:
        ordering = ('-created_at',)

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.file.name

    def __unicode__(self):
        return u'%s' % self.file.name

    def get_absolute_url(self):
        return reverse('app_samplefiles_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('app_samplefiles_update', args=(self.pk,))
