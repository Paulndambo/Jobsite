from django.urls import path
from . import views
from . views import *

urlpatterns = [
    path("", views.home, name="home"),
    path("job-seekers/", JobSeekers.as_view(), name="job-seekers"),
    path("job-seeker/<int:pk>/details", JobSeekerDetails.as_view(), name="job-seeker-details"),
    path("employers/", EmployersList.as_view(), name="employers"),
    path("employer-details/<int:pk>/", EmployerDetails.as_view(), name="employer-details"),
    path("kazi/", KaziList.as_view(), name="kazi"),
    path("kazi-details/<int:pk>/", KaziDetails.as_view(), name="kazi-details"),
]
