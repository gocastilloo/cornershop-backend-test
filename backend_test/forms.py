"""Forms to upload the menu."""
#Django
from django import forms

#Models
from .utils.models import Ingredients, Menu, User, Orders


class MenuForm(forms.Form):
    """Form based on model Menu"""
    dish_name = forms.CharField(
        max_length=150,
        required=True
    )
    description = forms.CharField(
        required=True
    )
    new_ingredients = forms.CharField()
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredients.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )
    image = forms.ImageField()


class OrderForm(forms.Form):
    """Form based on model Order"""
    menu = forms.ModelChoiceField(
        queryset=Menu.objects.all(),
        required=False)
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredients.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )
    quantity = forms.IntegerField(
        max_value=5,
    )
