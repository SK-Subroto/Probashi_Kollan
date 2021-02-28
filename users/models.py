from django.db import models
from django.contrib.auth.models import User
# from users.models import Country


class Country(models.Model):
    country_name = models.CharField(max_length=50, null=True)
    country_code = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.country_name


class Immigrant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    immigrant_id = models.CharField(max_length=20, null=True)
    national_id = models.CharField(max_length=30, null=True)
    immigrant_name = models.CharField(max_length=100, null=True)
    photo = models.ImageField(default="default_profile.jpg", null=True, blank=True)
    dob = models.DateField(null=True)
    job_status = models.BooleanField(default=False, null=True)
    job_desig = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    county = models.CharField(max_length=50, null=True)
    region = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    contact_nb = models.CharField(max_length=20, null=True)
    passport_nb = models.CharField(max_length=20, null=True)
    visa_nb = models.CharField(max_length=20, null=True)
    stay_duration = models.FloatField(null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Attendant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    attendant_id = models.CharField(max_length=20, null=True)
    attendant_name = models.CharField(max_length=100, null=True)
    photo = models.ImageField(default="default_profile_2.jpg", null=True, blank=True)
    dob = models.DateField(null=True)
    contact_nb = models.CharField(max_length=20, null=True)
    passport_nb = models.CharField(max_length=20, null=True)
    category = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
