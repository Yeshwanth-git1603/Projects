from django import forms

class CompanyForm(forms.Form):
    name = forms.CharField(max_length=100)
    origin = forms.CharField(max_length=100)
    ceo = forms.CharField(max_length=100)
    valuation = forms.CharField(max_length=100)
    type = forms.CharField(max_length=100)


