from django import forms

from app.models import Project, Sample, SampleFiles


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'is_public', 'status', 'startDate', 'endDate']


class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ['name', 'project', 'description', 'year_birth', 'is_male', 'bmi']


class SampleFilesForm(forms.ModelForm):
    class Meta:
        model = SampleFiles
        # fields = ['file_name', 'description', 'file', 'type', 'sample']
        fields = [ 'file', 'sample', 'description']
