from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.views.generic import UpdateView, ListView, CreateView, DetailView
from global_login_required import login_not_required

from app.forms import SampleForm, ProjectForm, SampleFilesForm
from app.models import Project, Sample, SampleFiles, CustomUser, Membership, UserRole

import logging as log

from app.util.helper import Message


def admin_dashboard(request):
    my_admin_projects = Project.objects.filter(member=request.user, membership__role=UserRole.ADMIN.value)
    print(my_admin_projects)
    return render(request, 'admin/dashboard.html', {'projects': my_admin_projects})
