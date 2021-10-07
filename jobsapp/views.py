from django.shortcuts import render
from . models import Employer, Job, Member
from django.views.generic import DetailView, ListView
# Create your views here.
def home(request):
    return render(request, "index.html")

class JobSeekers(ListView):
    model = Member
    template_name = "job-seekers.html"

class JobSeekerDetails(DetailView):
    model = Member
    template_name = "member-details.html"


class EmployersList(ListView):
    model = Employer
    template_name = "employers.html"

class EmployerDetails(DetailView):
    model = Employer
    template_name = "employer-details.html"

class KaziList(ListView):
    model = Job
    template_name = "kazi.html"

class KaziDetails(DetailView):
    model = Job
    template_name = "kazi-details.html"