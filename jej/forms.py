from django import forms

from jej.models import Author


class AddAuthorForm(forms.Form):
    first_name = forms.CharField(max_length=6, error_messages={'required':'Wypełnij to cholero'})
    last_name = forms.CharField(max_length=10, label='Nazwisko')


class AddBookForm(forms.Form):
    title = forms.CharField(max_length=20)
    author = forms.ModelChoiceField(queryset=Author.objects.all())



