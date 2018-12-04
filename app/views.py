from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.views.generic import UpdateView, ListView, CreateView, DetailView
from global_login_required import login_not_required

from app.forms import SampleForm, ProjectForm, SampleFilesForm
from app.models import Project, Sample, SampleFiles, CustomUser, Membership

import logging as log

from app.util.helper import Message


@login_not_required
def public_index(request):
    return render(request, 'public/index.html')


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

class ProjectViewMixin(UserPassesTestMixin):
    def test_func(self):
        pass


# class CheckUserIsProjectAdmin(LoginRequiredMixin):
#
#
# class UserPassesTestMixin(LoginRequiredMixin):
#     """Verify that the current user is authenticated."""
#
#
#
#     def get_project(self):
#
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

# LoginRequiredMixin,
class ProjectListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Project

    def get_queryset(self):
        u: CustomUser = self.request.user
        return Project.objects.filter(member=u)

    def test_func(self, **kwargs):
        # print("test ", self.object_list)
        # u: CustomUser = self.request.user
        ##res = CustomUser.objects.filter(project=self.model.)
        # print(res)
        return True


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        project: Project = form.instance
        user: CustomUser = self.request.user;
        project.created_by = user
        form.save()
        Membership.objects.create(project=project, user=user, role="admin")
        return super().form_valid(form)


class ProjectDetailView(DetailView):
    model = Project

    def get_object(self, queryset=None):
        project: Project = super(ProjectDetailView, self).get_object(queryset)
        if not Membership.is_user_project_member(project, self.request.user):
            raise Http404("dont have permission")

        return project


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm

    def get_object(self, queryset=None):
        p = super(ProjectUpdateView, self).get_object(queryset)
        #print(p)
        if not Membership.is_user_project_admin(p, self.request.user):
            raise Http404(Message.dont_have_permision)
        return p


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
