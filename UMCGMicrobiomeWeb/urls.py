import debug_toolbar

from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('admin_secret/', admin.site.urls),
    path('', include('app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('__debug__/', include(debug_toolbar.urls)),

    # accounts/login/ [name='login']
    # accounts/logout/ [name='logout']
    # accounts/password_change/ [name='password_change']
    # accounts/password_change/done/ [name='password_change_done']
    # accounts/password_reset/ [name='password_reset']
    # accounts/password_reset/done/ [name='password_reset_done']
    # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/reset/done/ [name='password_reset_complete']

    # path('login', auth_views.LoginView.as_view(template_name='login.html')),
    # url(r'^login$', 'django.contrib.auth.views.login'),

    # url(r'^login/$', 'django.contrib.auth.views.login', name='login'),

]
