# filepath: /home/shaytur/mealops/django-tutorial/recipes/forms.py
from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions', 'active']  # Use valid fields

    def clean(self):
        data = self.cleaned_data
        name = data.get("name")
        qs = Recipe.objects.filter(name__iexact=name)  # Check for case-insensitive exact match
        if qs.exists():
            self.add_error("name", f"\"{name}\" is already in use. Please pick another name.")
        return data        