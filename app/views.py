from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, DetailView

from app.forms import SampleForm, ProjectForm, SampleFilesForm
from app.models import Project, Sample, SampleFiles
from app.users.forms import CreateProjectForm
from django.contrib import messages

#from . import ProjectForm, SampleForm, SampleFilesForm
from . import views

from app.util.biom_test import ajde


# def demo_coreui1(request):
#     return render(request, 'demo_coreui1.html')


# def page1(request):
#     #    ajde()
#
#     return render(request, 'page1.html')


def public_index(request):
    return render(request, 'public/index.html')


# def login(request):
#     return render(request, 'login.html')
def dashboard(request):
    return render(request, 'dashboard.html')


# @permission_required("dsf")
# @login_required
# def projects(request):
#     my_projects = Project.objects.filter(user_admins=request.user)
#     return render(request, 'projects.html', {"projects": my_projects})


# def projects_new(request):
#     if request.method == 'POST':
#         form = CreateProjectForm(request.POST)
#
#         if form.is_valid():
#             new_project: Project = form.save(False)
#             new_project.user_creator = request.user
#
#             new_project.save()
#             new_project.user_admins.add(request.user)
#             new_project.save()
#             print(form.cleaned_data)
#
#             messages.add_message(request, messages.INFO, f"Successfully added project '{new_project.name}'.")
#             return HttpResponseRedirect(reverse('projects'))
#     else:
#         id = request.GET.get('id')
#         if id is not None:
#             project = get_object_or_404(Project, pk=id)
#             # TODO dodati validaciju
#             # if project.user_admins. != request.user:
#             #     return HttpResponseForbidden()
#             form = CreateProjectForm(instance=project)
#             print(project)
#         else:
#             form = CreateProjectForm()
#
#     return render(request, 'projects_new.html', {'form': form})


class ProjectListView(ListView):
    model = Project


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm


class ProjectDetailView(DetailView):
    model = Project


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm


class SampleListView(ListView):
    model = Sample


class SampleCreateView(CreateView):
    model = Sample
    form_class = SampleForm


class SampleDetailView(DetailView):
    model = Sample


class SampleUpdateView(UpdateView):
    model = Sample
    form_class = SampleForm


class SampleFilesListView(ListView):
    model = SampleFiles


class SampleFilesCreateView(CreateView):
    model = SampleFiles
    form_class = SampleFilesForm


class SampleFilesDetailView(DetailView):
    model = SampleFiles


class SampleFilesUpdateView(UpdateView):
    model = SampleFiles
    form_class = SampleFilesForm
