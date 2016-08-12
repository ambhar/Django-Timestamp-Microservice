from django import forms

class DateForm(forms.Form):
    check_date = forms.DateField()