from django import forms

class InventoryForm(forms.Form):
    frames = forms.IntegerField(required=True)
    products = forms.IntegerField(required=True)
    customers = forms.IntegerField(required=True)