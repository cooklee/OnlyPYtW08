from django import forms
from django.core.exceptions import ValidationError

from jej.models import Author, Book


def check_start_with_s(value):
    value = value.lower()
    if not value.startswith('s'):
        raise ValidationError("Autor musi zaczynać sie na s")


class AddAuthorForm(forms.Form):
    first_name = forms.CharField(max_length=20, error_messages={'required': 'Wypełnij to cholero'},
                                 widget=forms.Textarea)
    last_name = forms.CharField(max_length=20, label='Nazwisko', widget=forms.PasswordInput)

    def clean(self):
        data = super().clean()
        if data.get('first_name') == 'slawek' and data.get('last_name') == 'boguslawski':
            raise ValidationError("no nie tylko nie ten gosciu")


class AddBookForm(forms.Form):
    title = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Title'}), label='')
    author = forms.ModelChoiceField(queryset=Author.objects.all())


class AddBookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['year', 'author']
        widgets = {
            'year': forms.Textarea
        }
