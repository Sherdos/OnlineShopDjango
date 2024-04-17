from django import forms
from product.models import choices_review
from product.models import Review

class Review(forms.ModelForm):
    """Review definition."""
    assesment = forms.ChoiceField(choices=choices_review, widget=forms.Select(attrs={'class':'form-select d-inline-flex p-2 bd-highlight', }))
    class Meta:
        model = Review
        fields = ['text', 'assesment']
    
    # TODO: Define form fields here


