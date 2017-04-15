from django import forms

class FilterForm(forms.Form):
    clothing_type = forms.CharField(label='What type?', max_length=100)