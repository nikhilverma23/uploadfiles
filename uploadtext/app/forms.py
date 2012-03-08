from django.forms import forms


class Documentform(forms.Form):
    textfile = forms.FileField(label='Select a file')
