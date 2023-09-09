from django import forms
from datetime import date


BIRTH_YEAR_CHOICES = ["1980", "1981", "1982"]

CARD_LANK = [
    ("1", "Normal"),
    ("2", "Silber"),
    ("3", "Gold")
]

SHOPS_LIST = [
    ("1", "Shop A"),
    ("2", "Shop B"),
    ("3", "Shop C")
]

class PointCalculationForm(forms.Form):
    card_rank = forms.ChoiceField(label="", choices=CARD_LANK, required=False)
    order_date = forms.DateField(
        input_formats="%m%d%y",
        widget=forms.DateInput(attrs={"value":"2023-09-01", "type":"date"})
    )
    shop = forms.ChoiceField(label="", choices=SHOPS_LIST, required=False)
    order_price = forms.IntegerField(label="")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["card_rank"].widget.attrs.update({"class": "form-select mb-3"})
        self.fields["shop"].widget.attrs.update({"class": "form-select mb-3"})
        self.fields["order_date"].widget.attrs.update({
            "class": "form-select mb-3"
        })
        self.fields["order_price"].widget.attrs.update({"class": "form-control mb-3"})
