from django.forms import ModelForm
from django import forms
from .models import ImoItem

class createImoForm(ModelForm):
    user_name = forms.TextInput()
    user_opinion = forms.Textarea()
    class Meta:
        model = ImoItem
        fields = ['user_name', 'user_opinion']
