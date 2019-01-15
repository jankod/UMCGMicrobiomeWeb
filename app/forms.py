import logging

from django import forms

from app.models import Project, Sample, SampleFiles
from app.util.file_parser import FILE_TYPE_TAXONOMY, FILE_TYPE_TAXONOMY_MERGED, FILE_TYPE_PATHWAY, \
    FILE_TYPE_PATHWAY_MERGED

log = logging.getLogger("app")


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
        fields = ['file', 'sample', 'description']


class UploadFilesForm(forms.Form):
    project = forms.ModelChoiceField(queryset=Project.objects.none(), initial=0, required=True)
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    type = forms.ChoiceField(choices=[
        (FILE_TYPE_TAXONOMY, "Taxonomy"),
        (FILE_TYPE_TAXONOMY_MERGED, "Taxonomy merged"),
        (FILE_TYPE_PATHWAY, "Pathway"),
        (FILE_TYPE_PATHWAY_MERGED, "Pathway merged")
    ])

    def __init__(self, *args, user=None, **kwargs):
        super(UploadFilesForm, self).__init__(*args, **kwargs)
        # user = kwargs.pop('user', None)
        if user:
            log.debug("user %s", user)
            self.fields['project'].queryset = Project.objects.filter(membership__user=user)
