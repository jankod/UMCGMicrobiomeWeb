from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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


def projects_new(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)

        if form.is_valid():
            new_project: Project = form.save(False)
            new_project.user_creator = request.user

            new_project.save()
            print(form.cleaned_data)

            messages.add_message(request, messages.INFO, f"Successfully added project '{new_project.name}'.")
            return HttpResponseRedirect(reverse('projects'))
    else:
        form = CreateProjectForm()

    return render(request, 'projects_new.html', {'form': form})
