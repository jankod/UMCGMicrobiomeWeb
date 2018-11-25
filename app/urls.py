from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    path('', views.public_index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('demo_coreui1', views.demo_coreui1, name='demo_coreui1'),
    path('page1', views.page1, name='page1'),
    path('projects/', views.projects, name='projects'),
    path('projects/new', views.projects_new, name='project_new')


    # path('login', views.login, name='login'),
    #url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': '/login.html'}),


]
