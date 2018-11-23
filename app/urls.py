from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('demo_coreui1', views.demo_coreui1, name='demo_coreui1'),
    path('page1', views.page1, name='page1'),
    # path('login', views.login, name='login'),
    #url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': '/login.html'}),


]
