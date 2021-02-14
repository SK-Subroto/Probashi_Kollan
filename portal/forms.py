from django.forms import ModelForm
from .models import Test, Job, Blog


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = '__all__'


class JobFormAtten(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('attendant', 'date_posted',)


class blogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ('author', 'permission', 'date_posted',)


