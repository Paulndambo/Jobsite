from django.shortcuts import render
from jobsapp.models import *
from rest_framework import viewsets
from .serializers import *
# Create your views here.
class PositionViewSet(viewsets.ModelViewSet):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()

class EmployerViewSet(viewsets.ModelViewSet):
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()

class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

class EducationViewSet(viewsets.ModelViewSet):
    serializer_class = EducationSerializer
    queryset = Education.objects.all()

class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()

class HobbyViewSet(viewsets.ModelViewSet):
    serializer_class = HobbySerializer
    queryset = Hobby.objects.all()

class CertificateViewSet(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer
    queryset = Certificate.objects.all()

class RefereeViewSet(viewsets.ModelViewSet):
    serializer_class = RefereeSerializer
    queryset = Referee.objects.all()

class JobPostViewSet(viewsets.ModelViewSet):
    serializer_class = JobPostSerializer
    queryset = Job.objects.all()