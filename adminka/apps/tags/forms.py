from django import forms
from django.forms.widgets import TextInput
from .models import Tag


class ViewTag(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ViewTag, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {"class": "form-control", "disabled": "True"}
            )

    class Meta:
        model = Tag
        fields = ["name"]


class TagForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=TextInput(attrs={"type": "text", "class": "form-control"}),
    )

    class Meta:
        model = Tag
        fields = ["name"]
