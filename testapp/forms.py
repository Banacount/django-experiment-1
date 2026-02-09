from django.forms import ModelForm
from django import forms
from .models import UniversalChat


class SendChat(ModelForm):
    text = forms.TextInput()
    user_name = forms.TextInput()
    class Meta:
        model = UniversalChat
        fields = ['text', 'user_name']
