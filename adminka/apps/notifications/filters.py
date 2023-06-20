import django_filters
from .models import Notification
from django import forms


class NotificationFilter(django_filters.FilterSet):
    NOTIFICATION_TYPES = [
        ("success", "Positive"),
        ("warning", "Warning"),
        ("danger", "Error"),
        ("info", "Info"),
    ]

    text = django_filters.CharFilter(lookup_expr="icontains", field_name="text")
    text.field.widget = forms.TextInput(attrs={"type": "text", "class": "form-control"})

    start__gt = django_filters.CharFilter(lookup_expr="gt", field_name="start")
    start__gt.field.widget = forms.DateInput(
        attrs={"type": "date", "class": "form-control"}
    )

    start__lt = django_filters.CharFilter(lookup_expr="lt", field_name="start")
    start__lt.field.widget = forms.DateInput(
        attrs={"type": "date", "class": "form-control"}
    )

    end__gt = django_filters.CharFilter(lookup_expr="gt", field_name="end")
    end__gt.field.widget = forms.DateInput(
        attrs={"type": "date", "class": "form-control"}
    )

    end__lt = django_filters.CharFilter(lookup_expr="lt", field_name="end")
    end__lt.field.widget = forms.DateInput(
        attrs={"type": "date", "class": "form-control"}
    )

    type = django_filters.ChoiceFilter(field_name="type", choices=NOTIFICATION_TYPES)
    type.field.widget = forms.Select(
        attrs={"class": "form-control"}, choices=NOTIFICATION_TYPES
    )

    class Meta:
        model = Notification
        fields = ["text"]
