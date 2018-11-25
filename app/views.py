from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from app.models import Project


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
    my_projects = Project.objects.filter(project_admins=request.user)
    return render(request, 'projects.html', {"projects": my_projects})


def projects_new(request):
    return render(request, 'projects_new.html')
