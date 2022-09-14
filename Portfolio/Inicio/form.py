from django import forms
from .models import Mensajes


class MessageForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
