from django import forms
from django.contrib.auth.models import Group
from django.forms import TextInput

class ViewGroup(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ViewGroup, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'disabled': 'True'})

    class Meta:
        model = Group
        fields = ["name"]

        

class GroupForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=TextInput(attrs={"type": "text", "class": "form-control"}),
    )

    class Meta:
        model = Group
        fields = ["name"]