from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from app.models import Membership, Sample, SampleFiles, TaxonomyAbundance
from .models import CustomUser, Project
from app.users.forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'description']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Project)
admin.site.register(Sample)
admin.site.register(SampleFiles)
admin.site.register(TaxonomyAbundance)
admin.site.register(Membership)
