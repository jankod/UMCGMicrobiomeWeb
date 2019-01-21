import datetime
import os
from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ForeignKey
from django.urls import reverse


# PREMISSION_ADMIN = "admin"


class CustomUser(AbstractUser):
    description = models.TextField(max_length=40_000)

    def __str__(self):
        return f"{self.username} {self.email}"


class UserRole(Enum):
    ADMIN = 'admin'
    PARTICIPANT = 'participant'

    @staticmethod
    def admin_and_participant():
        return [UserRole.ADMIN.value, UserRole.PARTICIPANT.value]


class ProjectStatus(Enum):
    STARTED = "Started"
    ONGOING = "On going"
    ENDED = "Finished"


class Project(models.Model):
    NAME_LENGTH = 240
    DESCRIPTION_LENGTH = 40_000

    name = models.CharField(max_length=NAME_LENGTH)
    description = models.TextField(max_length=DESCRIPTION_LENGTH, blank=True, null=True)
    is_public = models.BooleanField(default=False, blank=False, null=False)
    status = models.CharField(blank=True, null=True, default=ProjectStatus.STARTED, max_length=20,
                              choices=[(tag.name, tag.value) for tag in ProjectStatus])
    startDate = models.DateField(blank=True, null=True, default=datetime.date.today)
    endDate = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Rel
    member = models.ManyToManyField(CustomUser, through='Membership', through_fields=('project', 'user'))
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_by')

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('app_project_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('app_project_update', args=(self.pk,))


class Membership(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # role = models.CharField(max_length=10)
    role = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in UserRole])

    def __str__(self):
        return f"{self.user.username}: '{self.project.name}' : {self.role}"

    @staticmethod
    def is_user_project_member(project: Project, user: CustomUser):
        members = Membership.objects.filter(project=project, user=user, role__in=UserRole.admin_and_participant())
        if not members:
            return False
        return True

    @staticmethod
    def is_user_project_admin(project, user):
        members = Membership.objects.filter(project=project, user=user, role__exact=UserRole.ADMIN.value)
        if not members:
            return False
        return True


class Sample(models.Model):
    NAME_LENGTH = 240
    DESCRIPTION_LENGTH = 40_000

    name = models.CharField(max_length=NAME_LENGTH)
    description = models.TextField(max_length=DESCRIPTION_LENGTH, blank=True, null=True)

    year_birth = models.SmallIntegerField(null=True, blank=True)
    is_male = models.BooleanField(null=True, blank=True)
    bmi = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
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
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, related_name="sample_files")

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


class TaxonomyIdAbundance(models.Model):
    abundance = models.DecimalField(decimal_places=10, max_digits=18)
    rank1_kingdom = models.IntegerField()
    rank2_phylum = models.IntegerField(null=True, blank=True)
    rank3_class = models.IntegerField(null=True, blank=True)
    rank4_order = models.IntegerField(null=True, blank=True)
    rank5_family = models.IntegerField(null=True, blank=True)
    rank6_genus = models.IntegerField(null=True, blank=True)
    rank7_species = models.IntegerField(null=True, blank=True)
    rank8_strain = models.IntegerField(null=True, blank=True)
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, related_name="sample_taxonomy_id_abundances")


def get_tax_id(tax_name: str) -> int:
    from django.core.cache import cache
    tax_id = cache.get(f"tax_{tax_name}")
    if tax_id is None:
        new_tax_name, created = TaxNames.objects.get_or_create(name=tax_name)
        cache.set(f"tax_{new_tax_name.id}", new_tax_name.id)
        tax_id = new_tax_name.id
    return tax_id


class TaxonomyAbundance(models.Model):
    abundance = models.DecimalField(decimal_places=10, max_digits=18)
    rank1_kingdom = models.CharField(max_length=30)
    rank2_phylum = models.CharField(max_length=70, null=True)
    rank3_class = models.CharField( max_length=100, null=True)
    rank4_order = models.CharField(max_length=100, null=True)
    rank5_family = models.CharField(max_length=100, null=True)
    rank6_genus = models.CharField(max_length=100, null=True)
    rank7_species = models.CharField(max_length=100, null=True)
    rank8_strain = models.CharField(max_length=100, null=True)
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE, related_name="sample_taxonomyabundances")

    def __str__(self):
        return f"{self.id} {self.abundance} {self.rank1_kingdom} {self.rank2_phylum}"

    def to_int_model(self) -> TaxonomyIdAbundance:
        tax_id_abundance: TaxonomyIdAbundance = TaxonomyIdAbundance()
        tax_id_abundance.abundance = self.abundance

        if self.rank1_kingdom is not None:
            tax_id_abundance.rank1_kingdom = get_tax_id(self.rank1_kingdom)

        if self.rank2_phylum is not None:
            tax_id_abundance.rank2_phylum = get_tax_id(self.rank2_phylum)

        if self.rank3_class is not None:
            tax_id_abundance.rank3_class = get_tax_id(self.rank3_class)

        if self.rank4_order is not None:
            tax_id_abundance.rank4_order = get_tax_id(self.rank4_order)

        if self.rank5_family is not None:
            tax_id_abundance.rank5_family = get_tax_id(self.rank5_family)

        if self.rank6_genus is not None:
            tax_id_abundance.rank6_genus = get_tax_id(self.rank6_genus)

        if self.rank7_species is not None:
            tax_id_abundance.rank7_species = get_tax_id(self.rank7_species)

        if self.rank8_strain is not None:
            tax_id_abundance.rank8_strain = get_tax_id(self.rank8_strain)

        return tax_id_abundance


class TaxNames(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]

# class Taxonomy(models.Model):
#     sample_file: ForeignKey(SampleFiles, on_delete=models.CASCADE, related_name="sample_file")


# class SampleStatistic(models.Model):
# Project_ID(link
# na
# Project)
# Metaphlan_PC1
# Metaphlan_PC2
# Metaphlan_PC3
# Metaphlan_tSNE_1
# Metaphlan_tSNE_2
# Metaphlan_tSNE_3
# Humann2_PC1
# Humann2_PC2
# Humann2_PC3
# Humann2_tSNE_1
# Humann2_tSNE_2
# Humann2_tSNE_3


# class ProjectStatistic(models.Model):
#     Sample
#     ID
#     Metaphlan_AD_Richness
#     float
#     Metaphlan_AD_Shannon
#     flaot
#     Metaphlan_AD_Simpson
#     float
#     Humann2_AD_Richness
#     float
#     Humann2_AD_Shannon
#     float
#     Humann2_AD_Simpson
#     float
