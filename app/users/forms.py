from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from app.models import CustomUser, Project


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'description')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'description')


class CreateProjectForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=Project.NAME_LENGTH)
    description = forms.Textarea()
    startDate = forms.DateField(label="Start date", help_text='ex. MM/DD/YYYY')
    endDate = forms.DateField(label="End date", help_text='ex. MM/DD/YYYY')

    class Meta:
        model = Project
        fields = ['name', 'description', 'is_public', 'startDate', 'endDate', 'status']
