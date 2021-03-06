# from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

# logging.getLogger('requests.packages.urllib3').setLevel(logging.ERROR)


urlpatterns = [
    path('', views.public_index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('upload_files', views.upload_files, name='upload_files')
    # views.UploadFilesView.as_view()


    # path('demo_coreui1', views.demo_coreui1, name='demo_coreui1'),
    # path('page1', views.page1, name='page1'),
    # path('projects/', views.projects, name='projects'),
    # path('projects/new', views.projects_new, name='project_new'),
    # # path('projects/edit/<int:pk>/', ProjectEditView.as_view(), name="project_edit"),

    # path('login', views.login, name='login'),
    # url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': '/login.html'}),

    # path('app/project/')
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

urlpatterns += (
    # ADMIN
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
