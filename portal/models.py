from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import Immigrant, Attendant


class Job(models.Model):
    attendant = models.ForeignKey(Attendant, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, null=True)
    job_type = models.CharField(max_length=100, null=True)
    area = models.CharField(max_length=100, null=True)
    company_name = models.CharField(max_length=100, null=True)
    vacancy = models.IntegerField(null=True)
    salary_scale = models.CharField(max_length=100, null=True)
    date_posted = models.DateTimeField(default=timezone.now, null=True)
    deadline = models.DateField(null=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    date_posted = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.title


# class Flight(models.Model):
#     flight_no
#     company_name
#     flight_type


class Chat(models.Model):
    sender = models.ForeignKey(Immigrant, null=True, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    mgs_posted = models.DateTimeField(default=timezone.now, null=True)
    mgs_body = models.TextField(null=True)

    def __str__(self):
        return self.sender
