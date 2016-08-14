from django import forms

class DateForm(forms.Form):
    check_date = forms.DateField(widget=forms.TextInput(attrs={'class' : 'form-control input-lg'}))