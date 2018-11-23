from django.urls import path

from . import views

urlpatterns = [
    path('', views.demo_coreui1, name='demo1'),
    path('page1', views.page1, name='page1'),

]
