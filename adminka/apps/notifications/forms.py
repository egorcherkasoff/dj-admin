from django import forms
from django.forms.widgets import TextInput, CheckboxInput, Select, DateInput
from .models import Notification


class NotificationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["allow_dates"].required = True

    NOTIFICATION_TYPES = [
        ("success", "Positive"),
        ("warning", "Warning"),
        ("danger", "Error"),
        ("info", "Info"),
    ]

    text = forms.CharField(
        max_length=100,
        widget=TextInput(attrs={"type": "text", "class": "form-control"}),
    )

    type = forms.ChoiceField(
        choices=NOTIFICATION_TYPES,
        widget=Select(attrs={"class": "form-control"}),
    )

    start = forms.DateField(
        widget=DateInput(attrs={"type": "date", "class": "form-control"}),
    )

    end = forms.DateField(
        widget=DateInput(attrs={"type": "date", "class": "form-control"}),
    )

    allow_dates = forms.BooleanField(
        required=False,
        widget=CheckboxInput(attrs={"class": "form-check-input"}),
    )

    class Meta:
        model = Notification
        fields = ["text", "type", "start", "end", "allow_dates"]


class ViewNotification(NotificationForm):
    def __init__(self, *args, **kwargs):
        super(ViewNotification, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"disabled": "True"})
