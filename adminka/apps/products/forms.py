from django import forms
from . import models
from django.forms import TextInput, Textarea, NumberInput, FileInput

class ViewProduct(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ViewProduct, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'disabled': 'True'})

    class Meta:
        model = models.Product
        fields = ["name", "description", "price", "amount"]

        

class ProductForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=TextInput(attrs={"type": "text", "class": "form-control"}),
    )

    description = forms.CharField(
        max_length=100,
        widget=Textarea(attrs={"class": "form-control"}),
    )

    price = forms.DecimalField(
        widget=NumberInput(attrs={"type": "number", "class": "form-control"}),
    )

    class Meta:
        model = models.Product
        fields = ["name", "description", "price"]


class ProductImagesForm(forms.ModelForm):
    image = forms.ImageField(widget=FileInput(attrs={"type": "file", "class": "form-control", "multiple": ""}))
    class Meta:
        model = models.ProductImage
        fields = ["image"]
