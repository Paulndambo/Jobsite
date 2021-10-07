from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
GENDER_CHOICES = (
    ("Female", "Female"),
    ("Male", "Male"),
    ("Binary", "Binary"),
)

AVAILABILITY_CHOICES = (
    ("Imediately", "Imediately"),
    ("Within 1 Week", "Within 1 Week"),
    ("Within 1 Month", "Within 1 Month"),
)

class Position(models.Model):
    title = models.CharField(max_length=500, unique=True, primary_key=True)
    description = models.TextField()
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    employer_id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    postal_code = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)
    date_joined = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    member_id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=500)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES)
    hours_per_week = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    postal_code = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)
    date_joined = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

class Education(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    level = models.CharField(max_length=500)
    achievements = models.CharField(max_length=500)
    award_or_certificate = models.CharField(max_length=500)
    graduated_or_graduating_on = models.DateField(default=timezone.now)

    def __str__(self):
        return self.member.name

class Skill(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    primary_skill = models.CharField(max_length=500)
    secondary_skill = models.CharField(max_length=500)
    third_skill = models.CharField(max_length=500)
    other_skills = models.CharField(max_length=500)

    def __str__(self):
        return self.member.name

class Certificate(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    certificate_title = models.CharField(max_length=500)
    awarded_by = models.CharField(max_length=500)
    date_awarded = models.DateField(default=timezone.now)

    def __str__(self):
        return self.member.name

class Hobby(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    hobby_1 = models.CharField(max_length=200)
    hobby_2 = models.CharField(max_length=200)
    hobby_3 = models.CharField(max_length=200)

    def __str__(self):
        return self.member.name

class Referee(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField()
    postal_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

LOCATION_CHOICES = (
    ("On-site", "On-site"),
    ("Remote", "Remote"),
)

JOB_CHOICES = (
    ("Permanent", "Permanent"),
    ("Contract", "Contract"),
    ("Part-Time", "Part-Time"),
    ("Full-Time", "Full-Time"),
)

SENIORITY_CHOICES = (
    ("Senior Level", "Senior Level"),
    ("Intermediate Level", "Intermediate Level"),
    ("Entry Level", "Entry Level"),
    ("Internship", "Internship"),
)


class Job(models.Model):
    title = models.CharField(max_length=500)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    salary = models.CharField(max_length=200)
    seniority_level = models.CharField(max_length=50, choices=SENIORITY_CHOICES, null=True)
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, null=True)
    job_type = models.CharField(max_length=50, choices=JOB_CHOICES, null=True)
    date_posted = models.DateField(default=timezone.now)
    verified = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return self.title