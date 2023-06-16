import django_filters
from .models import Product
from django import forms


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", field_name="name")
    name.field.widget = forms.TextInput(attrs={"type": "text", "class": "form-control"})

    price_gt = django_filters.NumberFilter(field_name="price", lookup_expr="gt")
    price_gt.field.widget = forms.NumberInput(
        attrs={"type": "number", "class": "form-control"}
    )

    price_lt = django_filters.NumberFilter(field_name="price", lookup_expr="lt")
    price_lt.field.widget = forms.NumberInput(
        attrs={"type": "number", "class": "form-control"}
    )

    created_gt = django_filters.DateFilter(field_name="created", lookup_expr="gt")
    created_gt.field.widget = forms.DateInput(
        attrs={"type": "date", "class": "form-control"}
    )
    
    created_lt = django_filters.DateFilter(field_name="created", lookup_expr="lt")
    created_lt.field.widget = forms.DateInput(
        attrs={"type": "date", "class": "form-control"}
    )

    amount_gt = django_filters.NumberFilter(field_name="amount", lookup_expr="gt")
    amount_gt.field.widget = forms.NumberInput(
        attrs={"type": "number", "class": "form-control"}
    )

    amount_lt = django_filters.NumberFilter(field_name="amount", lookup_expr="lt")
    amount_lt.field.widget = forms.NumberInput(
        attrs={"type": "number", "class": "form-control"}
    )

    class Meta:
        model = Product
        fields = ["name"]
