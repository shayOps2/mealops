from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Recipe.objects.filter(title__iexact=title) #sql query for incase sensetive exact match
        if qs.exists():
            self.add_error("title", f"\"{title}\" is already in use. Please pick another title.")
        return data
