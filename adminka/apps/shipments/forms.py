from django import forms
from .models import Shipment
from django.forms import TextInput, Textarea, NumberInput


class ViewShipment(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ViewShipment, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {"class": "form-control", "disabled": "True"}
            )

    class Meta:
        model = Shipment
        fields = ["series", "comment"]


class ShipmentForm(forms.ModelForm):
    series = forms.CharField(
        max_length=100,
        widget=TextInput(attrs={"type": "text", "class": "form-control"}),
    )

    comment = forms.CharField(
        max_length=255,
        widget=Textarea(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Shipment
        fields = ["series"]
