from django.contrib.auth.decorators import login_required
from django.shortcuts import render


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
    return render(request, 'projects.html')
