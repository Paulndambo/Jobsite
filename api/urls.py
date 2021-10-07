from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import *

router = DefaultRouter()

router.register("positions", PositionViewSet, basename="positions")
router.register("employers", EmployerViewSet, basename="employers")
router.register("freelancers", MemberViewSet, basename="freelancers")
router.register("education", EducationViewSet, basename="education")
router.register("skills", SkillViewSet, basename="skills")
router.register("hobbies", HobbyViewSet, basename="hobbies")
router.register("certificates", CertificateViewSet, basename="certificates")
router.register("referees", RefereeViewSet, basename="referees")
router.register("jobs", JobPostViewSet, basename="jobs")

urlpatterns = [
    path("", include(router.urls)),
]