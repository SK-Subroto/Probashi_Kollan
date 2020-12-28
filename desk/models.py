from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from users.models import Immigrant, Attendant


class Meeting(models.Model):
    attendant = models.ForeignKey(Attendant, null=True, on_delete=models.SET_NULL)
    immigrant = models.ForeignKey(Immigrant, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    date_posted = models.DateTimeField(default=timezone.now, null=True)
    meeting_date = models.DateTimeField(null=True)
    meeting_status = models.BooleanField(default=False,null=True, blank=True)

    def __str__(self):
        return self.title


class Notice(models.Model):
    author = models.ForeignKey(Attendant, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    date_posted = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.title
