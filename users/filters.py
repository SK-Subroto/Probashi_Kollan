import django_filters
from django_filters import DateFilter, CharFilter

from .models import Immigrant


class ImmigrantFilter(django_filters.FilterSet):
    immigrant_name = CharFilter(field_name='user__first_name', lookup_expr='icontains', label='Name')

    class Meta:
        model = Immigrant
        fields = ['immigrant_name', 'region']