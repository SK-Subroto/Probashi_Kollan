from rest_framework import serializers
from .models import Attendant, Immigrant
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('is_active',)


class ImmigrantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Immigrant
        fields = '__all__'
        depth = 2
