import django_filters
from django_filters import DateFilter, CharFilter

from .models import Notice


class NoticeFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_posted", lookup_expr='gte', label='Start Date')
    end_date = DateFilter(field_name="date_posted", lookup_expr='lte', label='End Date')
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title')

    class Meta:
        model = Notice
        fields = '__all__'
        exclude = ['author', 'description', 'date_posted']
