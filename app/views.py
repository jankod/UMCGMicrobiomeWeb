from django.shortcuts import render


def demo_coreui1(request):
    return render(request, 'demo_coreui1.html')


def page1(request):
    return render(request, 'page1.html')
