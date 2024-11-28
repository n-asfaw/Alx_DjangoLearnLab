# bookshelf/forms.py
from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False)
    
class ExampleForm(forms.Form):
    # Define form fields here, for example:
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)