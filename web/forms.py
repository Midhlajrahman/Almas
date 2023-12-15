from django import forms
from django.forms import widgets

from .models import (
    ProductEnquiry
)

class ProductEnquiryForm(forms.ModelForm):
    class Meta:
        model = ProductEnquiry
        exclude = ("product",)
        widgets = {
            "name": widgets.TextInput(attrs={"class": "required form-control"}),
            "phone": widgets.TextInput(attrs={"class": "required form-control"}),
            "email": widgets.EmailInput(attrs={"class": "required form-control"}),
        }