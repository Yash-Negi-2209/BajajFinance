from django import forms

class JSONInputForm(forms.Form):
    data = forms.CharField(widget=forms.Textarea, label='JSON Input')
