from django import forms


class SimpleForm(forms.Form):
    massage_to_print = forms.CharField(max_length=100)