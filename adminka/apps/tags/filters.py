import django_filters
from .models import Tag
from django import forms

class TagFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", field_name="name")
    name.field.widget = forms.TextInput(attrs={"type":"text", "class":"form-control"})
    
    created_gt = django_filters.DateFilter(lookup_expr="gt", field_name="created")
    created_gt.field.widget = forms.DateInput(attrs={"type":"date", "class":"form-control"})
    
    created_lt = django_filters.DateFilter(lookup_expr="lt", field_name="created")
    created_lt.field.widget = forms.DateInput(attrs={"type":"date", "class":"form-control"})


    class Meta:
        model = Tag
        fields = ["name"]