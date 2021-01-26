from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Immigrant
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class ImmigrantForm(ModelForm):
    class Meta:
        model = Immigrant
        fields = ('contact_nb', 'passport_nb')