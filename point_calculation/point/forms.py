from django import forms
from .models import Shop, Product

CARD_LANK = [
    ("1", "Normal"),
    ("2", "Silber"),
    ("3", "Gold")
]

class PointCalculationForm(forms.Form):
    card_rank = forms.ChoiceField(label="", choices=CARD_LANK, required=False)
    order_date = forms.DateField(widget=forms.DateInput(attrs={"value":"2023-09-01", "type":"date"}))
    shop = forms.ModelChoiceField(required=True, queryset=Shop.objects.all())
    product = forms.ModelChoiceField(required=True, queryset=Product.objects.all())
 
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set widget for MDB 
        self.fields["card_rank"].widget.attrs.update({"class": "form-select mb-3"})
        self.fields["order_date"].widget.attrs.update({
            "class": "form-select mb-3"
        })
        self.fields["shop"].widget.attrs.update({"class": "form-select mb-3"})
        self.fields["product"].widget.attrs.update({"class": "form-select mb-3"})
