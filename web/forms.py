from django import forms
from django.forms import widgets

from .models import Contact, Enquiry, Product, ProductEnquiry


class ProductEnquiryForm(forms.ModelForm):
    class Meta:
        model = ProductEnquiry
        exclude = ("product",)
        widgets = {
            "name": widgets.TextInput(
                attrs={"class": "required form-control", "placeholder": "Your Name"}
            ),
            "phone": widgets.TextInput(
                attrs={"class": "required form-control", "placeholder": "Your Number"}
            ),
            "email": widgets.EmailInput(
                attrs={"class": "required form-control", "placeholder": "Your Email"}
            ),
            "message": widgets.TextInput(
                attrs={"class": "required form-control", "placeholder": "Your message"}
            ),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("",)
        widgets = {
            "name": widgets.TextInput(
                attrs={"class": " input-box", "placeholder": "Your Name"}
            ),
            "phone": widgets.TextInput(
                attrs={"class": "input-box", "placeholder": "Your Number"}
            ),
            "email": widgets.EmailInput(
                attrs={"class": "input-box", "placeholder": "Your email"}
            ),
            "subject": widgets.TextInput(
                attrs={"class": "input-box", "placeholder": "Your subject"}
            ),
            "message": widgets.Textarea(
                attrs={"class": "input-box", "placeholder": "Your message"}
            ),
        }


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ["service", "name", "email", "message"]
        widgets = {
            "name": widgets.TextInput(
                attrs={"class": "input-box", "placeholder": "Your Name"}
            ),
            "email": widgets.EmailInput(
                attrs={"class": "input-box", "placeholder": "Your email"}
            ),
            "service": widgets.Select(
                attrs={"class": "input-box", "placeholder": "Service You Need"}
            ),
            "message": widgets.Textarea(
                attrs={"class": "input-box", "placeholder": "Your message"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(EnquiryForm, self).__init__(*args, **kwargs)
        self.fields["service"].queryset = Product.objects.all()
