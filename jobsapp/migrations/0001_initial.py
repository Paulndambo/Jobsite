# Generated by Django 3.2.5 on 2021-07-28 22:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('employer_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=500)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('postal_code', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('verified', models.BooleanField(default=False)),
                ('date_joined', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=500)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Binary', 'Binary')], max_length=20)),
                ('availability', models.CharField(choices=[('Imediately', 'Imediately'), ('Within 1 Week', 'Within 1 Week'), ('Within 1 Month', 'Within 1 Month')], max_length=20)),
                ('hours_per_week', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('postal_code', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('verified', models.BooleanField(default=False)),
                ('date_joined', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('title', models.CharField(max_length=500, primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField()),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('primary_skill', models.CharField(max_length=500)),
                ('secondary_skill', models.CharField(max_length=500)),
                ('third_skill', models.CharField(max_length=500)),
                ('other_skills', models.CharField(max_length=500)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobsapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='Referee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Binary', 'Binary')], max_length=20)),
                ('phone_number', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('postal_code', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobsapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('salary', models.CharField(max_length=200)),
                ('seniority_level', models.CharField(choices=[('Senior Level', 'Senior Level'), ('Intermediate Level', 'Intermediate Level'), ('Entry Level', 'Entry Level'), ('Internship', 'Internship')], max_length=50)),
                ('location', models.CharField(choices=[('On-site', 'On-site'), ('Remote', 'Remote')], max_length=50)),
                ('job_type', models.CharField(choices=[('Permanent', 'Permanent'), ('Contract', 'Contract'), ('Part-Time', 'Part-Time'), ('Full-Time', 'Full-Time')], max_length=50)),
                ('description', models.TextField()),
                ('date_posted', models.DateField(default=django.utils.timezone.now)),
                ('verified', models.BooleanField(default=False)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobsapp.employer')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobsapp.position')),
            ],
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('hobby_1', models.CharField(max_length=200)),
                ('hobby_2', models.CharField(max_length=200)),
                ('hobby_3', models.CharField(max_length=200)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobsapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('level', models.CharField(max_length=500)),
                ('achievements', models.CharField(max_length=500)),
                ('award_or_certificate', models.CharField(max_length=500)),
                ('graduated_or_graduating_on', models.DateField(default=django.utils.timezone.now)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobsapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('certificate_title', models.CharField(max_length=500)),
                ('awarded_by', models.CharField(max_length=500)),
                ('date_awarded', models.DateField(default=django.utils.timezone.now)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobsapp.member')),
            ],
        ),
    ]
