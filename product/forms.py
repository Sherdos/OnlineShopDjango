from django import forms
from product.models import choices_review
from product.models import Review
from user.models import CartProduct


class ReviewForm(forms.ModelForm):
    """Review definition."""
    assesment = forms.ChoiceField(choices=choices_review, widget=forms.Select(attrs={'class':'form-select d-inline-flex p-2 bd-highlight', }))
    class Meta:
        model = Review
        fields = ['text', 'assesment']
    
    # TODO: Define form fields here

class CartProductForm(forms.ModelForm):
    class Meta:
        model = CartProduct
        fields = ('count','size')
        widgets = {
            'count':forms.NumberInput(attrs={'class':'form-control'}),
            'size':forms.Select(attrs={'class':'form-select d-inline-flex p-2 bd-highlight', })
        }