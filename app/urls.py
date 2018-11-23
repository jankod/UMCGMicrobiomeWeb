from django.urls import path

from . import views

urlpatterns = [
    path('', views.demo_coreui1, name='demo1'),


]
