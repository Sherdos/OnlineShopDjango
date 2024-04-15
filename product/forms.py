from django import forms
choice = (
 ('1','1'),
 ('2','2'),
 ('3','3'),
 ('4','4'),
 ('5','5'),
 ('6','6'),
 ('7','7'),
 ('8','8'),
 ('9','9'),
 ('10','10'),
)
class Review(forms.Form):
    """Review definition."""
    review = forms.ChoiceField(choices=choice, widget=forms.Select(attrs={'class':'form-select d-inline-flex p-2 bd-highlight', }))
    
    
    # TODO: Define form fields here

