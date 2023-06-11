import django_filters
from .models import User
from django import forms

class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr="icontains", field_name="first_name")
    first_name.field.widget = forms.TextInput(attrs={"type":"text", "class":"form-control"})
    
    middle_name = django_filters.CharFilter(lookup_expr="icontains", field_name="middle_name")
    middle_name.field.widget =forms.TextInput (attrs={"type":"text", "class":"form-control"})
    
    last_name = django_filters.CharFilter(lookup_expr="icontains", field_name="last_name")
    last_name.field.widget = forms.TextInput(attrs={"type":"text", "class":"form-control"})
    
    email = django_filters.CharFilter(lookup_expr="icontains")
    email.field.widget = forms.EmailInput(attrs={"type":"email", "class":"form-control"})
    
    date_joined = django_filters.DateFilter(lookup_expr="contains", field_name="date_joined")
    date_joined.field.widget = forms.DateInput(attrs={"type":"date", "class":"form-control"})
    
    date_joined_gt = django_filters.DateFilter(lookup_expr="gt", field_name="date_joined")
    date_joined_gt.field.widget = forms.DateInput(attrs={"type":"date", "class":"form-control"})
    
    date_joined_lt = django_filters.DateFilter(lookup_expr="lt", field_name="date_joined")
    date_joined_lt.field.widget = forms.DateInput(attrs={"type":"date", "class":"form-control"})


    class Meta:
        model = User
        fields = ["email", "date_joined", "first_name", "last_name", "middle_name"]