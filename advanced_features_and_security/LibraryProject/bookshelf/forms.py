# bookshelf/forms.py
from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False)
