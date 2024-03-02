from django import forms

class createDescription(forms.Form):
    description = forms.CharField(label='Description', max_length=1000)