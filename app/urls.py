# from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

# from app.views import ProjectEditView
from . import views

urlpatterns = [
    path('', views.public_index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),

    # path('demo_coreui1', views.demo_coreui1, name='demo_coreui1'),
    # path('page1', views.page1, name='page1'),
    # path('projects/', views.projects, name='projects'),
    # path('projects/new', views.projects_new, name='project_new'),
    # # path('projects/edit/<int:pk>/', ProjectEditView.as_view(), name="project_edit"),

    # path('login', views.login, name='login'),
    # url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': '/login.html'}),

]



urlpatterns += (
    # urls for Project
    path('app/project/', views.ProjectListView.as_view(), name='app_project_list'),
    path('app/project/create/', views.ProjectCreateView.as_view(), name='app_project_create'),
    path('app/project/detail/<int:pk>/', views.ProjectDetailView.as_view(), name='app_project_detail'),
    path('app/project/update/<int:pk>/', views.ProjectUpdateView.as_view(), name='app_project_update'),
)

urlpatterns += (
    # urls for Sample
    path('app/sample/', views.SampleListView.as_view(), name='app_sample_list'),
    path('app/sample/create/', views.SampleCreateView.as_view(), name='app_sample_create'),
    path('app/sample/detail/<int:pk>/', views.SampleDetailView.as_view(), name='app_sample_detail'),
    path('app/sample/update/<int:pk>/', views.SampleUpdateView.as_view(), name='app_sample_update'),
)

urlpatterns += (
    # urls for SampleFiles
    path('app/samplefiles/', views.SampleFilesListView.as_view(), name='app_samplefiles_list'),
    path('app/samplefiles/create/', views.SampleFilesCreateView.as_view(), name='app_samplefiles_create'),
    path('app/samplefiles/detail/<int:pk>/', views.SampleFilesDetailView.as_view(), name='app_samplefiles_detail'),
    path('app/samplefiles/update/<int:pk>/', views.SampleFilesUpdateView.as_view(), name='app_samplefiles_update'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
