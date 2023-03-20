import django_filters
from .models import LogProc
from django import forms


class ProcessLogFilter(django_filters.FilterSet):
    eventtime = django_filters.DateTimeFromToRangeFilter(field_name='eventtime', lookup_expr='icontains',
                                                         widget=django_filters.widgets.RangeWidget(
                                                             attrs={'type': 'datetime-local'}))
    proc = django_filters.CharFilter(field_name='proc', lookup_expr='icontains',
                                     widget=forms.TextInput())
    text = django_filters.CharFilter(field_name='text', lookup_expr='icontains',
                                     widget=forms.TextInput(
                                         attrs={"class": "form-control", "max_length": "80",
                                                'style': 'margin-bottom:8px; width: 220px'}))
    obj_type = django_filters.CharFilter(field_name='obj_type', lookup_expr='icontains',
                                         widget=forms.TextInput())
    err_dtl = django_filters.CharFilter(field_name='err_dtl', lookup_expr='icontains',
                                        widget=forms.TextInput())

    class Meta:
        model = LogProc
        fields = ['eventtime', 'proc', 'text', 'obj_type', 'err_dtl']

