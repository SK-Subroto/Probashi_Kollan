from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Immigrant, Attendant
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class ImmigrantForm(ModelForm):
    class Meta:
        model = Immigrant
        fields = ('national_id', 'contact_nb', 'passport_nb', 'region')


class ImmigrantUpdateForm(ModelForm):
    class Meta:
        model = Immigrant
        fields = '__all__'
        exclude = ('user', 'immigrant_id', 'immigrant_name', 'national_id', 'county')
        widgets = {
            'photo': forms.FileInput(),
        }


class AttendantUpdateForm(ModelForm):
    class Meta:
        model = Attendant
        fields = '__all__'
        exclude = ('user', 'attendant_id', 'attendant_name', 'category')
        widgets = {
            'photo': forms.FileInput(),
        }

