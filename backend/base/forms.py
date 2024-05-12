from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    production_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = Product
        fields = "__all__"
