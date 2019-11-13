from django import forms

from resi import models


class BookForms(forms.Form):
    name = forms.CharField(max_length=120,
                           widget=forms.TextInput(
                               attrs={
                                   "one": "one",
                               }
                           ),
                           error_messages={},
                           help_text="书名",
                           required=True,
                           validators={},

                           )
    price = forms.DecimalField(max_digits=5, decimal_places=2)
    img = forms.CharField(max_length=150,)
    authors = forms.ModelMultipleChoiceField(queryset=models.Author.objects.all())


class PublishForm(forms.ModelForm):
    class Meta:
        model = models.Publish
        fields = ["name", 'address']


