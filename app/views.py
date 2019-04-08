import logging
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from typing import List, Any, Union

from django.core.files.uploadedfile import InMemoryUploadedFile

from app.forms import UploadFilesForm
from app.models import TaxonomyAbundance
from app.util.file_parser import parse_taxonomy_file, FILE_TYPE_TAXONOMY, TaxonomyAbundanceParserResult, \
    FILE_TYPE_TAXONOMY_MERGED, parse_taxonomy_merged_file, TaxonomyParserResult
from app.util.helper import Message
# import logging as log
from app.views_admin import *

# Get an instance of a logger
log = logging.getLogger("app")


@login_not_required
def public_index(request):
    log.info("public page")
    return render(request, 'public/index.html')


def dashboard(request):
    return render(request, 'dashboard.html')


# class UploadFilesView(FormView):
#     form_class = UploadFilesForm
#     template_name = 'upload_files.html'
#     success_url = 'upload_files.html'
#
#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('files')
#         if form.is_valid():
#             for f in files:
#                 ...  # Do something with each file.
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)


def upload_files(request):
    if request.method == 'POST':
        log.debug("request.user %s", request.user)
        form = UploadFilesForm(request.POST, request.FILES, user=request.user, )
        messages = []
        if form.is_valid():
            # files = form.cleaned_data['files']
            files = request.FILES.getlist('files')
            file_type = form.cleaned_data['type']
            project = form.cleaned_data['project']
            if file_type == FILE_TYPE_TAXONOMY:
                for f in files:
                    tax_parse_result = parse_taxonomy_file(f)
                    messages.extend(handle_one_sample_taxonomy(project, tax_parse_result))
            if file_type == FILE_TYPE_TAXONOMY_MERGED:
                for f in files:
                    result: List[TaxonomyParserResult] = parse_taxonomy_merged_file(f)
                    for tax_parser_result in result:
                        messages.extend(handle_one_sample_taxonomy(project, tax_parser_result))

            form = UploadFilesForm(user=request.user)
            return render(request, 'upload_files.html',
                          {'form': form, 'message': 'Sve ok uneseno u formu', 'messages': messages})
    else:
        form = UploadFilesForm(user=request.user)

    return render(request, 'upload_files.html', {'form': form, 'message': ''})


def handle_one_sample_taxonomy(project: Project, tax_parse_result: TaxonomyParserResult) -> List[str]:
    messages = []
    sample: Sample = Sample.objects.filter(name=tax_parse_result.sample_name).first()
    if sample is not None:
        messages.append(f"Exist sample {tax_parse_result.sample_name}, remove prijasnje rezultate")
        TaxonomyAbundance.objects.filter(sample=sample).delete()
    else:
        messages.append(f"Create new sample {tax_parse_result.sample_name} in project {project.name}")
        sample = Sample.objects.create(name=tax_parse_result.sample_name, project=project)
        sample.save()

    tax_parse_result.normalise()


    tax: TaxonomyAbundanceParserResult
    taxes = []
    for tax in tax_parse_result.taxonomy_abundances:
        if tax.abundance == 0:
            continue
        tax = tax.to_model()
        tax_int = tax.to_int_model()
        tax.sample = sample
        taxes.append(tax)
        if len(taxes) > 5_000:
            log.debug(f"spremam  5 000 njih prvo")
            TaxonomyAbundance.objects.bulk_create(taxes)
            taxes.clear()

    log.debug(f"spremam u bazu  ostatak od {len(taxes)} redova za sample {sample.name}, bilo ih je {len(tax_parse_result.taxonomy_abundances)}")
    TaxonomyAbundance.objects.bulk_create(taxes)
    log.debug(f"gotovo")

    messages.append(f"Add {len(taxes)} taxonomy-abundances into db")
    return messages


# @permission_required("dsf")
# @login_required
# def projects(request):
#     my_projects = Project.objects.filter(user_admins=request.user)
#     return render(request, 'projects.html', {"projects": my_projects})


# def projects_new(request):
#     if request.method == 'POST':
#         form = CreateProjectForm(request.POST)
#
#         if form.is_valid():
#             new_project: Project = form.save(False)
#             new_project.user_creator = request.user
#
#             new_project.save()
#             new_project.user_admins.add(request.user)
#             new_project.save()
#             print(form.cleaned_data)
#
#             messages.add_message(request, messages.INFO, f"Successfully added project '{new_project.name}'.")
#             return HttpResponseRedirect(reverse('projects'))
#     else:
#         id = request.GET.get('id')
#         if id is not None:
#             project = get_object_or_404(Project, pk=id)

#             # if project.user_admins. != request.user:
#             #     return HttpResponseForbidden()
#             form = CreateProjectForm(instance=project)
#             print(project)
#         else:
#             form = CreateProjectForm()
#
#     return render(request, 'projects_new.html', {'form': form})

class ProjectViewMixin(UserPassesTestMixin):
    def test_func(self):
        pass


# class CheckUserIsProjectAdmin(LoginRequiredMixin):
#
#
# class UserPassesTestMixin(LoginRequiredMixin):
#     """Verify that the current user is authenticated."""
#
#
#
#     def get_project(self):
#
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

# LoginRequiredMixin,
class ProjectListView(UserPassesTestMixin, ListView):
    model = Project

    def get_queryset(self):
        u: CustomUser = self.request.user
        return Project.objects.filter(member=u)

    def test_func(self, **kwargs):
        return True


class ProjectCreateView(CreateView):
    # Ko si moze raditi projekt? ????
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        project: Project = form.instance
        user: CustomUser = self.request.user
        project.created_by = user
        form.save()
        Membership.objects.create(project=project, user=user, role=UserRole.ADMIN.value)
        return super().form_valid(form)


class ProjectDetailView(DetailView):
    model = Project

    def get_object(self, queryset=None):
        project: Project = super(ProjectDetailView, self).get_object(queryset)
        if not Membership.is_user_project_member(project, self.request.user):
            raise Http404("dont have permission")

        return project


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm

    def get_object(self, queryset=None):
        p = super(ProjectUpdateView, self).get_object(queryset)
        if not Membership.is_user_project_admin(p, self.request.user):
            raise Http404(Message.dont_have_permission)
        return p


class SampleListView(ListView):
    model = Sample

    def get_queryset(self):
        u: CustomUser = self.request.user
        membership = Membership.objects.filter(user=u)
        project_ids = []
        m: Membership
        for m in membership:
            project_ids.append(m.project.id)

        print("Nasao project ids ", project_ids)
        return Sample.objects.filter(project__in=project_ids)


class SampleCreateView(CreateView):
    model = Sample
    form_class = SampleForm

    def get_object(self, queryset=None):
        super()


class SampleDetailView(DetailView):
    model = Sample


class SampleUpdateView(UpdateView):
    model = Sample
    form_class = SampleForm


class SampleFilesListView(ListView):
    model = SampleFiles
    paginate_by = 10

    def get_queryset(self):
        q = super(SampleFilesListView, self).get_queryset()
        q = q.prefetch_related('sample', 'sample__project')
        return q


class SampleFilesCreateView(CreateView):
    model = SampleFiles
    form_class = SampleFilesForm


class SampleFilesDetailView(DetailView):
    model = SampleFiles


class SampleFilesUpdateView(UpdateView):
    model = SampleFiles
    form_class = SampleFilesForm
