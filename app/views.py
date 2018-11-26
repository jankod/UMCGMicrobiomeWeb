from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import UpdateView

from app.models import Project
from app.users.forms import CreateProjectForm
from django.contrib import messages


def demo_coreui1(request):
    return render(request, 'demo_coreui1.html')


def page1(request):
    return render(request, 'page1.html')


def public_index(request):
    request.user.is_authenticated
    return render(request, 'public/index.html')


# def login(request):
#     return render(request, 'login.html')
def dashboard(request):
    return render(request, 'dashboard.html')


def projects(request):
    my_projects = Project.objects.filter(user_admins=request.user)
    return render(request, 'projects.html', {"projects": my_projects})


class ProjectEditView(UpdateView):
    model = Project
    form_class = CreateProjectForm
    success_url = reverse('projects')
    template_name = 'projects_edit.html'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)


def projects_new(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)

        if form.is_valid():
            new_project: Project = form.save(False)
            new_project.user_creator = request.user

            new_project.save()
            new_project.user_admins.add(request.user)
            new_project.save()
            print(form.cleaned_data)

            messages.add_message(request, messages.INFO, f"Successfully added project '{new_project.name}'.")
            return HttpResponseRedirect(reverse('projects'))
    else:
        id = request.GET.get('id')
        if id is not None:
            project = get_object_or_404(Project, pk=id)
            # TODO dodati validaciju
            # if project.user_admins. != request.user:
            #     return HttpResponseForbidden()
            form = CreateProjectForm(instance=project)
            print(project)
        else:
            form = CreateProjectForm()

    return render(request, 'projects_new.html', {'form': form})
