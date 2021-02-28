import django_filters
from django_filters import DateFilter, CharFilter

from .models import Job, Blog


class JobFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Post')

    class Meta:
        model = Job
        fields = ['title', 'company_name', 'region']


class BlogFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_posted", lookup_expr='gte', label='Start Date')
    end_date = DateFilter(field_name="date_posted", lookup_expr='lte', label='End Date')
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title')

    class Meta:
        model = Blog
        fields = ['title', 'region']
