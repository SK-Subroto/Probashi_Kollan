from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import Immigrant, Attendant, Country
from ckeditor.fields import RichTextField


class Job(models.Model):
    attendant = models.ForeignKey(Attendant, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, null=True)
    company_name = models.CharField(max_length=100, null=True)
    company_logo = models.URLField(max_length=500, null=True)
    date_posted = models.DateTimeField(default=timezone.now, null=True)
    deadline = models.DateField(null=True)
    body = RichTextField(blank=True, null=True)
    region = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Blog(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    date_posted = models.DateTimeField(default=timezone.now, null=True)
    photo = models.ImageField(null=True, blank=True)
    permission = models.BooleanField(default=False, null=True)
    region = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


# class Flight(models.Model):
#     flight_no
#     company_name
#     flight_type


class Test(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Chat(models.Model):
    sender = models.ForeignKey(Immigrant, null=True, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    mgs_posted = models.DateTimeField(default=timezone.now, null=True)
    mgs_body = models.TextField(null=True)

    def __str__(self):
        return self.sender
