from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def demo_coreui1(request):
    return render(request, 'demo_coreui1.html')

@login_required
def page1(request):
    return render(request, 'page1.html')


def index(request):
    request.user.is_authenticated
    return render(request, 'index.html')


# def login(request):
#     return render(request, 'login.html')
