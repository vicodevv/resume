from django import forms
from django.forms import fields
from .models import Contact

class ContactForm(forms.Form):
    class Meta:
        model = Contact
        fields = "__all__"
