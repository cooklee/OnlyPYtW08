from django import forms


class AddAuthorForm(forms.Form):
    first_name = forms.CharField(max_length=6)
    last_name = forms.CharField(max_length=10, label='Nazwisko')



