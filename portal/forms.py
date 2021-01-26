from django.forms import ModelForm
from .models import Test, Job


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = '__all__'


class JobFormAtten(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('attendant', 'date_posted',)